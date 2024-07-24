import datetime

from django.test import TestCase

from accounts.models import *

class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user_1 = User.objects.create(
            username='user1',
            first_name="name1",
            last_name="surname1"
        )

        user_2 = User.objects.create(
            username='user2',
            first_name="name2",
            last_name="surname2"
        )

        user_3 = User.objects.create(
            username='user3',
            first_name="name3",
            last_name="surname3"
        )

        user_4 = User.objects.create(
            username='user4',
            first_name="name4",
            last_name="surname4"
        )

        profile_1 = Profile.objects.create(
            phone_number='0325485369',
            date_of_birth=datetime.date(1960, 10, 10),
            billing_address='billing_address1',
        )

        profile_2 = Profile.objects.create(
            phone_number='0325484598',
            date_of_birth=datetime.date(1970, 11, 1),
            billing_address='billing_address2',
        )

        profile_3 = Profile.objects.create(
            phone_number='0482685369',
            date_of_birth=datetime.date(1980, 1, 12),
            billing_address='billing_address3',
        )

        profile_4 = Profile.objects.create(
            phone_number='0325457369',
            date_of_birth=datetime.date(1990, 3, 18),
            billing_address='billing_address4',
        )

        profile_1.user = user_1
        profile_2.user = user_2
        profile_3.user = user_3
        profile_4.user = user_4

        profile_1.save()
        profile_2.save()
        profile_3.save()
        profile_4.save()

        order_1 = Order.objects.create(
            profile=profile_3,
            delivery_address='delivery_address1',
            total="22.48",
            date_of_creation=datetime.date(2024, 3, 10),
        )

        order_2 = Order.objects.create(
            profile=profile_3,
            delivery_address='delivery_address2',
            total="120.88",
            date_of_creation=datetime.date(2023, 10, 28),
        )

        order_1.profile = profile_3
        order_1.save()
        order_2.profile = profile_3
        order_2.save()

        # product_1 = Product.objects.create(
        #     title="Product 1",
        #     price="2.48",
        #     stock=30
        # )
        #
        # product_2 = Product.objects.create(
        #     title="Product 2",
        #     price="3.68",
        #     stock=50
        # )
        #
        # order_product_1 = OrderProduct.objects.create(
        #     order=order_1,
        #     # product='product_1',
        #     quantity="10",
        # )
        #
        # order_product_2 = OrderProduct.objects.create(
        #     order=order_1,
        #     # product='product_2',
        #     quantity="20",
        # )
        #
        # order_product_3 = OrderProduct.objects.create(
        #     order=order_1,
        #     # product='product_4',
        #     quantity="20",
        # )
        #
        # order_product_4 = OrderProduct.objects.create(
        #     order=order_2,
        #     # product='product_3',
        #     quantity="20",
        # )
        #
        # order_product_5 = OrderProduct.objects.create(
        #     order=order_2,
        #     # product='product_2',
        #     quantity="20",
        # )


    def setUp(self):
        print('-'*80)

    def test_profile_phone(self):
        profile = Profile.objects.get(id=1)
        print(f"test_profile_phone: '{profile.phone_number}'")
        self.assertEqual(profile.phone_number, "0325485369")

    def test_profile_repr(self):
        profile = Profile.objects.get(id=1)
        print(f"test_profile_repr: '{profile.__repr__()}'")
        self.assertEqual(profile.__repr__(), "Profile(user=surname1 name1)")

    def test_profile_str(self):
        profile = Profile.objects.get(id=3)
        print(f"test_profile_str: '{profile.__str__()}'")
        self.assertEqual(profile.__str__(), "surname3 name3")

    def test_profile_orders_count(self):
        profile_3 = Profile.objects.get(id=3)
        orders_count = Order.objects.filter(profile=profile_3).count()
        print(f"test_profile_orders_count: {orders_count}")
        self.assertEqual(orders_count, 2)

    def test_profile_str(self):
        profile = Profile.objects.get(id=3)
        print(f"test_profile_str: '{profile.__str__()}'")
        self.assertEqual(profile.__str__(), "surname3 name3")

