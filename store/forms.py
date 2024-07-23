from django.forms import *

from store.models import *
class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        initial_title = self.cleaned_data['title']
        return initial_title.strip().capitalize()

class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        initial_title = self.cleaned_data['title']
        return initial_title.strip().capitalize()


