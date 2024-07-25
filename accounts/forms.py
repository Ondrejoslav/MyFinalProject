from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.transaction import atomic
from django.forms import *

from accounts.models import *
from store.models import Product
from datetime import date


# class SignUpForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']
#
#     phone_number = CharField(label = 'Phone number')
#     date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}))
#     billing_address = CharField(label='Billing address', widget=Textarea)
#
#     def clean(self):
#         initial_data = super().clean()
#         date_of_birth = initial_data.get('date_of_birth')
#         if date_of_birth >= date.today():
#             raise ValidationError('Only past dates are allowed!')
#         return initial_data
#
#     @atomic
#     def save(self, commit=True):
#         self.instance.is_active = True
#         user = super().save(commit)
#         phone_number = self.cleaned_data['phone_number']
#         date_of_birth = self.cleaned_data['date_of_birth']
#         billing_address = self.cleaned_data['billing_address']
#         profile = Profile(user=user, phone_number=phone_number,
#                           date_of_birth=date_of_birth, billing_address=billing_address)
#         if commit:
#             profile.save()
#         return user


class UserProductModelForm(ModelForm):
    class Meta:
        model = UserProduct
        fields = ['quantity']
        widgets = {
            'quantity': NumberInput(attrs={'min': 1, }) # For some reason, it enables to set the upper limit only
        }

    # quantity = IntegerField(min_value=1, max_value=10) #This did not work
    # quantity = IntegerField(default=2, validators=[MaxValueValidator(100), MinValueValidator(1)]) # Neither did this


class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address']