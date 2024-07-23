from concurrent.futures._base import LOGGER

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from store.forms import *
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
    if Product.objects.filter(pk=pk).exists():
        product = Product.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'product.html', context)
    return products(request)


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class CategoryCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CategoryModelForm
    success_url = reverse_lazy('categories')
    permission_required = 'store.add_category'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Category
    form_class = CategoryModelForm
    success_url = reverse_lazy('categories')
    permission_required = 'store.change_category'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class CategoryDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'category_confirm_delete.html'
    model = Category
    success_url = reverse_lazy('categories')
    permission_required = 'store.delete_category'


class ProductCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products')
    permission_required = 'store.add_product'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Product
    form_class = ProductModelForm
    success_url = reverse_lazy('products')
    permission_required = 'store.change_product'

    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


class ProductDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('products')
    permission_required = 'store.delete_product'