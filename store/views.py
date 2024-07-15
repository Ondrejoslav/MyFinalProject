from concurrent.futures._base import LOGGER

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from store.forms import CustomerModelForm
from store.models import *


def home(request):
    return render(request, 'home.html')


def categories(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)


def category(request, pk):
    if Category.objects.filter(id=pk).exists():
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
        context = {'category': category, 'products': products}
        return render(request, 'category.html', context)
    return categories(request)


def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def products_and_categories(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {'categories': categories, 'products': products}
    return render(request, 'products_and_categories.html', context)


def product(request, pk):
    if Product.objects.filter(id=pk).exists():
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product.html', context)
    return products(request)


class CustomerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CustomerModelForm
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)

