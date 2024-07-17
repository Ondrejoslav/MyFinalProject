from django.forms import *

from accounts.models import *


class ProfileProductModelForm(ModelForm):
    class Meta:
        model = ProfileProduct
        fields = ['quantity']