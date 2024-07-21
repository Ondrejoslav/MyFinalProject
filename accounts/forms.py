from django.forms import *

from accounts.models import *


class UserProductModelForm(ModelForm):
    class Meta:
        model = UserProduct
        fields = ['quantity']

class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address']