from django.contrib import admin

from accounts.models import *

admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(UserProduct)