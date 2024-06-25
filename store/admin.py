from django.contrib import admin

from store.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderProduct)


