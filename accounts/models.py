from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField, DateField, CharField, BooleanField, \
    DateTimeField, ForeignKey, DO_NOTHING, DecimalField, IntegerField, PositiveIntegerField, ImageField

from store.models import Category, Product


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, null=True, blank=True)
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
    profile = ForeignKey(Profile, on_delete=DO_NOTHING, null=True, blank=True)
    delivery_address = TextField(default='Fill in this field only if it differs from the billing address')
    total = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_of_creation = DateTimeField(auto_now_add=False, null=True, blank=True, default=None)

    class Meta:
        ordering = ['date_of_creation', 'profile__user__last_name', 'profile__user__first_name']

    def __str__(self):
        return (f'Id: {self.id}, customer: {self.profile.user.first_name} {self.profile.user.last_name}, '
                f'birthdate: {self.profile.date_of_birth}, billing address: {self.profile.billing_address},'
                f'delivery address: {self.delivery_address}, date of creation: {self.date_of_creation}')


class OrderProduct(Model):
    order = ForeignKey(Order, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    quantity = IntegerField()

    class Meta:
        ordering = ['order__date_of_creation', 'product__title']

    def __str__(self):
        return f'id of the order: {self.order.id}, item: {self.product.title}, quantity: {self.quantity}'


class UserProduct(Model):
    user = ForeignKey(User, on_delete=DO_NOTHING, null=True, blank=True)
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    quantity = PositiveIntegerField(null=True, blank=True)

    class Meta:
        ordering = ['user__last_name', 'product__title']

    def __str__(self):
        return f'username: {self.user}, item: {self.product.title}, quantity: {self.quantity}'


