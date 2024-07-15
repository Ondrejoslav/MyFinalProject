from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.db.transaction import atomic
from django.forms import DateField, CharField, Textarea, NumberInput, ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from accounts.models import Profile


# Create your views here.

class SubmittableLoginView(LoginView):
    template_name = 'registration/login.html'


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    phone_number = CharField(label = 'Phone number')
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}))
    billing_address = CharField(label='Billing address', widget=Textarea)

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        phone_number = self.cleaned_data['phone_number']
        date_of_birth = self.cleaned_data['date_of_birth']
        billing_address = self.cleaned_data['billing_address']
        profile = Profile(user=user, phone_number=phone_number,
                          date_of_birth=date_of_birth, billing_address=billing_address)
        if commit:
            profile.save()
        return user


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('home')


@ login_required
def users(request): #TODO: Change functional view for class-based view
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'profiles.html', context)


@ login_required
def user(request, pk):
    if User.objects.filter(id=pk).exists():
        user = User.objects.get(pk=pk)
        context = {'user': user}
        return render(request, 'profile_detail.html', context)
    return users(request)


# class UserModelForm(ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'