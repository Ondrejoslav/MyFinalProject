import datetime

from django.test import TestCase

from store.models import *
from store.forms import CategoryModelForm, ProductModelForm


class CategoryFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        def test_category_form_is_valid(self):
            form = CategoryModelForm(
            data={
                'title': '   Crucibles   ',
            }
        )
            print(f"\ntest_people_form_is_valid: {form.data}")
            self.assertTrue(form.is_valid())


class ProductFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        def test_product_form_is_valid(self):
            form = CategoryModelForm(
            data={
                'title': '   Crucibles   ',
            }
            )
            print(f"\ntest_people_form_is_valid: {form.data}")
            self.assertTrue(form.is_valid())