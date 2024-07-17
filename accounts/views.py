from concurrent.futures._base import LOGGER

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.exceptions import PermissionDenied
from django.db.transaction import atomic
from django.forms import DateField, CharField, Textarea, NumberInput, ModelForm, IntegerField, Form
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, UpdateView, DeleteView

from accounts.forms import ProfileProductModelForm
from accounts.models import Profile, Order, ProfileProduct
from store.models import Product
from store.views import product


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
def user(request):
    return render(request, 'profile_detail.html')


@ login_required
def add_to_cart(request, pk):
    profile = Profile.objects.get(user=request.user)
    product = Product.objects.get(pk=pk)
    quantity = 1
    profile_product = ProfileProduct(profile=profile, product=product, quantity=quantity)
    profile_product.save()
    context={'profile_product': profile_product}
    return render(request, 'item.html', context)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = ProfileProduct
    form_class = ProfileProductModelForm
    success_url = reverse_lazy('your_cart')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data while updating a creator.')
        return super().form_invalid(form)


class ItemDeleteView(DeleteView):
    template_name = 'item_confirm_delete.html'
    model = ProfileProduct
    success_url = reverse_lazy('cart')


@login_required
def your_cart(request):
    profile = Profile.objects.get(user=request.user)
    profile_products = ProfileProduct.objects.filter(profile=profile)
    total = 0
    for profile_product in profile_products:
        total += profile_product.product.price * profile_product.quantity
    context = {'profile_products': profile_products, 'total': total}
    return render(request, 'cart.html', context)


@ login_required
def your_orders(request):
    orders = Order.objects.filter(profile__user=request.user)
    context = {'orders': orders}
    return render(request, 'orders.html', context)