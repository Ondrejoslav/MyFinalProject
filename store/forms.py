from django.forms import *

from store.models import *


# class CustomerModelForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'   # TODO: set up a user friendly date format
#
#     def clean_name(self):
#         initial_name = self.cleaned_data['name']  # původní name od uživatele
#         return initial_name.strip().capitalize()


