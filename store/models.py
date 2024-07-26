from django.db.models import *
#from accounts.models import *


class Category(Model):
    title = CharField(max_length=50)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "categories"

    def __repr__(self):
        return f'<title: {self.title}>'

    def __str__(self):
        return self.title


class Image(Model):
    image = ImageField(upload_to='images/', default='default_image.png', null=False, blank=False)
    description = TextField(null=True, blank=True)

    def __repr__(self):
        return f'Image(image = {self.image}, description = {self.description})'

    def __str__(self):
        return f'Image: {self.image}, {self.description}'


class Product(Model):
    title = CharField(max_length=50)
    category = ForeignKey(Category, on_delete=DO_NOTHING)
    description = TextField()
    price = DecimalField(max_digits=10, decimal_places=2)
    stock = IntegerField()
    image = ForeignKey(Image, on_delete=DO_NOTHING, null=True, blank=True)

    class Meta:
        ordering = ['title']

    def __repr__(self):
        return f'<title: {self.title}>'

    def __str__(self):
        return f'{self.title} ({self.category})'


