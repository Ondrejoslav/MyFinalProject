from django.db.models import *


class Category(Model):
    title = CharField(max_length=50)

    def __str__(self):
        return self.title


class Product(Model):
    title = CharField(max_length=50)
    category = ForeignKey(Category, on_delete=CASCADE)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = IntegerField()

    def __repr__(self):
        return self.title


class Cart(Model):
    created_at = DateTimeField(auto_now_add=True)

    # add a function that calculates the total cost
    # add a function that updates the stock count for the products concerned


class Order(Model):
    customer_full_name = CharField(max_length=50)
    date_of_birth = DateField()
    customer_billing_address = CharField(max_length=50)
    # house_number = CharField(max_length=15)
    # street = CharField(max_length=30)
    # city = CharField(max_length=30)
    # postal_code = CharField(max_length=15)
    # country = CharField(max_length=20)
    customer_delivery_address = CharField(max_length=50)
    customer_email = CharField(max_length=50)
    customer_phone = CharField(max_length=15)
    order_placed_at = DateTimeField(auto_now_add=True)
    order_price_total = DecimalField(max_digits=10, decimal_places=2)

    # apply the function that calculates the total cost


class Customer(Model):
    full_name = CharField(max_length=50)
    email = EmailField()
