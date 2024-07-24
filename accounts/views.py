from datetime import datetime, date
from concurrent.futures._base import LOGGER

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.core.exceptions import PermissionDenied, ValidationError
from django.contrib.sessions.middleware import SessionMiddleware
from django.db.transaction import atomic
from django.forms import DateField, CharField, Textarea, NumberInput, ModelForm, IntegerField, Form
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, FormView, UpdateView, DeleteView, ListView

from accounts.forms import UserProductModelForm, OrderModelForm
from accounts.models import Profile, Order, UserProduct, OrderProduct
from store.models import Product
from store.views import product


class SubmittableLoginView(LoginView):
    template_name = 'registration/login.html'


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']

    phone_number = CharField(label = 'Phone number')
    date_of_birth = DateField(widget=NumberInput(attrs={'type': 'date'}))
    billing_address = CharField(label='Billing address', widget=Textarea)

    def validate(self, date_of_birth):
        super().validate(date_of_birth)
        if date_of_birth >= date.today():
            raise ValidationError('Only past dates are allowed!')


    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)
        phone_number = self.cleaned_data['phone_number']
        date_of_birth = self.cleaned_data['date_of_birth']
        billing_address = self.cleaned_data['billing_address']
        profile = Profile(user=user, phone_number=phone_number,
                          date_of_birth=date_of_birth, billing_address=billing_address)
        if commit:
            profile.save()
        return user


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('home')


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('home')


@ login_required
def users(request): #TODO: Change functional view for class-based view
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'profiles.html', context)


@ login_required
def user(request):
    return render(request, 'profile_detail.html')


def add_to_cart(request, pk):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = request.session.session_key
    product = Product.objects.get(pk=pk)
    if UserProduct.objects.filter(user=user, product=product).exists():
        user_product = UserProduct.objects.get(user=user, product=product)
    else:
        quantity = 1
        user_product = UserProduct(user=user, product=product, quantity=quantity)
        user_product.save()
    context = {'user_product': user_product}
    return render(request, 'item.html', context)


# @login_required
def discard_item(request, pk):
    user_product = UserProduct.objects.get(pk=pk)
    product = user_product.product
    user_product.delete()
    context = {'product': product}
    return render(request, 'product.html', context)


class ItemUpdateView(UpdateView):
    template_name = 'form.html'
    model = UserProduct
    form_class = UserProductModelForm
    success_url = reverse_lazy('your_cart')

    def form_invalid(self, form):
        LOGGER.warning('You have provided invalid data!')
        return super().form_invalid(form)


class ItemDeleteView(DeleteView):
    template_name = 'item_confirm_delete.html'
    model = UserProduct
    success_url = reverse_lazy('your_cart')


def remove_item_from_cart(request, pk):
    if UserProduct.objects.filter(pk=pk).exists():
        UserProduct.objects.get(pk=pk).delete()
    return your_cart(request)


# @login_required
def your_cart(request):
    if request.user.is_authenticated:
        user=request.user
    else:
        user=request.session.session_key
    user_products_orig = UserProduct.objects.filter(user=user)
    exceeds_number = ''
    total = 0
    for user_product in user_products_orig:
        if user_product.quantity > user_product.product.stock:
            max_quantity = user_product.product.stock
            user_product.quantity = max_quantity
            user_product.save()
            exceeds_number = user_product.product.title
        total += user_product.product.price * user_product.quantity
        if user_product.quantity == 0:
            user_product.delete()
    user_products = UserProduct.objects.filter(user=user)
    if exceeds_number != '':
        notice_a = 'The demanded quantity for the last added product ('
        notice_b = ') exceeded the stock and was changed accordingly!'
        context = {'user_products': user_products, 'total': total, 'exceeds_number': exceeds_number,
                   'notice_a': notice_a, 'notice_b': notice_b}
        return render(request, 'cart.html', context)
    context = {'user_products': user_products, 'total': total}
    return render(request, 'cart.html', context)

# @login_required
def empty_cart(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = request.session.session_key
    UserProduct.objects.filter(user=user).delete()
    return your_cart(request)


# @login_required
def cart_confirm_delete(request):
    if request.user.is_authenticated:
        user=request.user
    else:
        user=request.session.session_key
    if UserProduct.objects.filter(user=user).exists():
        user_products = UserProduct.objects.filter(user=user)
        context = {'user_products': user_products}
        return render(request, 'cart_confirm_delete.html', context)
    else:
        return your_cart(request)


@ login_required
def place_order(request):
    user = request.user
    if UserProduct.objects.filter(user=user).exists():
        profile = Profile.objects.get(user=user)
        delivery_address = '==not entered yet=='
        order = Order(profile=profile, delivery_address=delivery_address)
        user_products = UserProduct.objects.filter(user=user)
        total = 0
        for user_product in user_products:
            total += user_product.product.price * user_product.quantity
        order.total = total
        order.save()
        uncleaned_list_of_orders = Order.objects.filter(profile=profile)
        for examined_order in uncleaned_list_of_orders:
            if examined_order.id != order.id and examined_order.date_of_creation == order.date_of_creation:
                examined_order.delete()
        context = {'order': order}
        return render(request, 'setting_up_order.html', context)
    return your_cart(request)


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Order
    form_class = OrderModelForm
    permission_required = 'accounts.change_order'

    def get_success_url(self):
        return reverse_lazy('order_preview', kwargs={'pk': self.object.pk})


    def form_invalid(self, form):
        LOGGER.warning('User provided invalid data.')
        return super().form_invalid(form)


@ login_required
def order_preview(request, pk):
    user = request.user
    order = Order.objects.get(pk=pk)
    if order.delivery_address == '==not entered yet==':
        order.delivery_address = '==The same as billing address=='
        order.save()
    user_products = UserProduct.objects.filter(user=user)
    context = {'order': order, 'user_products': user_products}
    return render(request, 'order_preview.html', context)


@ login_required
def order_confirmation(request, pk):
    user = request.user
    user_products = UserProduct.objects.filter(user=user)
    order = Order.objects.get(pk=pk)
    if OrderProduct.objects.filter(order=order).exists():
        return order_summary(request, pk)
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_of_creation = datetime.fromtimestamp(timestamp)
    order.date_of_creation = date_of_creation
    order.save()
    for user_product in user_products:
        order_product = OrderProduct(order=order, product=user_product.product, quantity=user_product.quantity)
        order_product.save()
        id_product = user_product.product.id
        product = Product.objects.get(pk=id_product)
        product.stock = product.stock - user_product.quantity
        product.save()
    user_products.delete()
    context = {'order': order}
    return render(request, 'thank_you_page.html', context)


@ login_required
def order_decline(request, pk):
    user = request.user
    order = Order.objects.get(pk=pk)
    if order.profile.user.id != user.id:
        return your_orders(request)
    if OrderProduct.objects.filter(order=order).exists():
        return order_summary(request, pk)
    order.delete()
    return your_cart(request)


@login_required
def order_summary(request, pk):
    user = request.user
    order = Order.objects.get(pk=pk)
    if order.profile.user.id != user.id:
        return your_orders(request)
    order_products = OrderProduct.objects.filter(order=order)
    payment_deadline = datetime.fromtimestamp(order.date_of_creation.timestamp() + 30*24*60*60)
    context = {'order': order, 'order_products': order_products, 'payment_deadline': payment_deadline}
    return render(request, 'order_summary.html', context)


@ login_required
def your_orders(request):
    orders = Order.objects.filter(profile__user=request.user)
    context = {'orders': orders}
    return render(request, 'orders.html', context)


class OrdersListView(PermissionRequiredMixin, ListView):
    template_name = "orders_overview.html"
    model = Order
    context_object_name = 'all_orders'
    permission_required = 'accounts.view_order'