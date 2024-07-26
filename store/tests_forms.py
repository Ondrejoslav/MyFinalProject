from django.test import TestCase

from store.views import *
from store.forms import CategoryModelForm, ProductModelForm


class CategoryFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(title='category_1')
        Category.objects.create(title='category_2')
        Category.objects.create(title='category_3')

    def test_category_form_is_valid(self):
        form = CategoryModelForm(
            data={
                    'title': 'category_4'
                }
        )
        print(f"\ntest_category_form_is_valid: {form.data}")
        self.assertTrue(form.is_valid())


class ProductFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Product.objects.create(title='product_1')
        Product.objects.create(cost='2.50')
        Product.objects.create(stock='50')

        def test_product_form_is_valid(self):
            form = ProductModelForm(
            data={
                'title': 'product_4',
                'category': '3',
                'description': 'some description',
                'price': '5.50',
                'stock': '50'
            }
            )
            print(f"\ntest_people_form_is_valid: {form.data}")
            self.assertTrue(form.is_valid())
