from django.db.models import *


class Category(Model):
    title = CharField(max_length=50)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "categories"

    def __repr__(self):
        return f'<title: {self.title}>'

    def __str__(self):
        return self.title


class Product(Model):
    title = CharField(max_length=50)
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = IntegerField()

    class Meta:
        ordering = ['title']

    def __repr__(self):
        return f'<title: {self.title}>'

    def __str__(self):
        return f'{self.title} ({self.category})'


class Image(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ImageField()
    description = TextField()