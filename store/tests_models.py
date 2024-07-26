import datetime

from django.test import TestCase

from store.models import *

class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):

        category_flasks = Category.objects.create(title="Flasks")
        # category_flasks = Category.objects.create(title="Flasks")
        category_funnels = Category.objects.create(title="Funnels")
        category_cylinders = Category.objects.create(title="Cylinders")
        category_tubes = Category.objects.create(title="Tubes")
        category_beakers = Category.objects.create(title="Beakers")
        category_bottles = Category.objects.create(title="Bottles")
        category_condensers = Category.objects.create(title="Condensers")


        product_1 = Product.objects.create(
            category=category_flasks,
            title="Round Bottom 2 Neck Jointed Flask 100 ml",
            description="Volume: 100 ml\r\nGround joint: 24/29 (centre),  14/23 (angle)",
            price="29.34",
            stock=20
        )

        product_2 = Product.objects.create(
            category=category_flasks,
            title="Round Bottom 3 Neck Jointed Flask 100 ml",
            description="Volume: 100 ml Ground joints: 19/26 (central), 14/23 (angles)",
            price="30.94",
            stock=30
        )

        product_3 = Product.objects.create(
            category=category_flasks,
            title="Erlenmeyer Jointed Flask 50 ml",
            description="Volume: 50 ml\r\nGround joint: 14/23",
            price="13.74",
            stock=100
        )

        product_4 = Product.objects.create(
            category=category_funnels,
            title="Separating Jointed Funnel",
            description="Volume: 100 ml\r\nGround joint: 19/26",
            price="71.98",
            stock=50
        )

        product_5 = Product.objects.create(
            category=category_funnels,
            title="Filter Funnel Short Stem",
            description="Stem length: 55 mm",
            price="1.88",
            stock=120
        )

        product_6 = Product.objects.create(
            category=category_cylinders,
            title="Measuring Cylinder Hex. Base 100 ml",
            description="White graduations",
            price="2.48",
            stock=120
        )


    def setUp(self):
        print('-'*80)

    def test_product_title(self):
        product = Product.objects.get(id=1)
        print(f"test_product_title: '{product.title}'")
        self.assertEqual(product.title, "Round Bottom 2 Neck Jointed Flask 100 ml")

    def test_product_repr(self):
        product = Product.objects.get(id=1)
        print(f"test_product_repr: '{product.__repr__()}'")
        self.assertEqual(product.__repr__(), "<title: Round Bottom 2 Neck Jointed Flask 100 ml>")

    def test_product_str(self):
        product = Product.objects.get(id=1)
        print(f"test_product_str: '{product}'")
        self.assertEqual(product.__str__(), "Round Bottom 2 Neck Jointed Flask 100 ml (Flasks)")

    def test_category_products_count(self):
        category = Category.objects.get(id=1)
        number_of_products = Product.objects.filter(category=category).count()
        print(f"test_category_products_count: {number_of_products}")
        self.assertEqual(number_of_products, 3)

    def test_category_unique(self):
        categories = Category.objects.filter(title="Flasks").count()
        print(f"test_category_unique: count={categories}")
        self.assertEqual(categories, 1)

    def test_absence_of_product(self):
        product_count = Product.objects.filter(title="Beaker").count()
        print(f"test_absence_of_product: count={product_count}")
        self.assertEqual(product_count, 0)
