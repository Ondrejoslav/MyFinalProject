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
        return self.title


class Image(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ImageField()
    description = TextField()


class Customer(Model):
    full_name = CharField(max_length=50)
    email = EmailField()
    phone = CharField(max_length=15)
    date_of_birth = DateField()
    billing_address = TextField()
    subscribed_to_newsletters = BooleanField()
    date_of_registration = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


class Order(Model):
    customer = ForeignKey(Customer, on_delete=DO_NOTHING)
    delivery_address = TextField()
    total = DecimalField(max_digits=10, decimal_places=2)
    date_of_creation = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_of_creation']

    def __str__(self):
        return f'customer: {self.customer}, date of creation: {self.date_of_creation}'


class OrderProduct(Model):
    order = ForeignKey(Order, on_delete=DO_NOTHING)
    product = ForeignKey(Product, on_delete=DO_NOTHING)
    quantity = IntegerField()

    class Meta:
        ordering = ['order', 'product']

    def __str__(self):
        return f'{self.order}, item: {self.product}, quantity: {self.quantity}'

