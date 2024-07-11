from concurrent.futures._base import LOGGER

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView

from store.models import *


class CustomerModelForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

    def clean_name(self):
        initial_name = self.cleaned_data['name']  # původní name od uživatele
        return initial_name.strip().capitalize()


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CustomerModelForm
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)