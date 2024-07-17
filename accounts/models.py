from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField, DateField, CharField, BooleanField, \
    DateTimeField, ForeignKey, DO_NOTHING, DecimalField, IntegerField

from store.models import Category, Product, Image


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='has_profile')
    phone_number = CharField(max_length=15, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    billing_address = TextField(null=True, blank=True)
    # subscribed_to_newsletters = BooleanField()   #TODO: This might be worth doing
    # date_of_registration = DateTimeField(auto_now_add=True)  #TODO: This might be worth doing

    class Meta:
        ordering = ['user__last_name', 'user__first_name']

    def __repr__(self):
        return f'Profile(user={self.user.last_name} {self.user.first_name})'

    def __str__(self):
        return f'{self.user.last_name} {self.user.first_name}'


class Order(Model):
    profile = ForeignKey(Profile, on_delete=DO_NOTHING, related_name='orders')
    delivery_address = TextField()
    total = DecimalField(max_digits=10, decimal_places=2)
    date_of_creation = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_of_creation', 'profile__user__last_name', 'profile__user__first_name']

    def __str__(self):
        return (f'customer: {self.profile.user.last_name}{self.profile.user.first_name}, '
                f'date of creation: {self.date_of_creation}')


class OrderProduct(Model):
    order = ForeignKey(Order, on_delete=DO_NOTHING)
    product = ForeignKey(Product, on_delete=DO_NOTHING, related_name='related_order')
    quantity = IntegerField()

    class Meta:
        ordering = ['order__date_of_creation', 'product__title']

    def __str__(self):
        return f'{self.order}, item: {self.product}, quantity: {self.quantity}'

    # def calculate_total(self):
    #     total = 0
    #     for item in {cart}:
    #         total += item.price * cart[item]
    #     return total
    #
    # def empty_cart(self):
    #     cart = {}
    #     return cart
    #
    # def add_number(self, number):
    #     x=0
    #     x+=number
    #     return x


class ProfileProduct(Model):
    profile = ForeignKey(Profile, on_delete=DO_NOTHING, related_name='containing')
    product = ForeignKey(Product, on_delete=DO_NOTHING, related_name='is_in')
    quantity = IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['profile__user__last_name', 'product__title']

    def __str__(self):
        return (f'Customer: {self.profile.user.last_name} {self.profile.user.last_name}'
                f'item: {self.product.title}, quantity: {self.quantity}')