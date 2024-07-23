from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import *

from accounts.models import *
from store.models import Product

class UserProductModelForm(ModelForm):
    class Meta:
        model = UserProduct
        fields = ['quantity']
        widgets = {
            'quantity': NumberInput(attrs={'min': 1, }) # For some reason, it sets the upper limit only
        }

    # quantity = IntegerField(min_value=1, max_value=10) #This did not work
    # quantity = IntegerField(default=2, validators=[MaxValueValidator(100), MinValueValidator(1)]) # Neither did this


class OrderModelForm(ModelForm):
    class Meta:
        model = Order
        fields = ['delivery_address']