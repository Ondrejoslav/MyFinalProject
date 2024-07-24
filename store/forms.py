import re

from django.forms import *

from store.models import *


class CategoryModelForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_title(self):
        initial_title = self.cleaned_data['title']
        return (" ".join(initial_title.split())).title()

class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        initial_title = self.cleaned_data['title']
        return (" ".join(initial_title.split())).title()

    def clean_description(self):
        # Force each sentence of the description to be capitalized.
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)


