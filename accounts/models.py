from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, TextField, DateField, CharField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE, related_name='has_profile')
    phone_number = CharField(max_length=15, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    billing_address = TextField(null=True, blank=True)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f'Profile(user={self.profile})'

    def __str__(self):
        return f'{self.profile}'

