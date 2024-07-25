"""labware_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

import rest_framework
from django.conf.urls.static import static

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

import api
from api.views import *
from accounts.views import *
from labware_store import settings
from store.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('category/create/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<pk>/', category, name='category'),
    path('products/', products, name='products'),
    path('products_and_categories/', products_and_categories, name='products_and_categories'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<pk>/', product, name='product'),

    # path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'), # customized login view
    path('accounts/signup/', SignUpView.as_view(), name='signup'), # customized signup view
    path('accounts/password_change/', SubmittablePasswordChangeView.as_view(), name='password_change'), # customized password change view
    path('accounts/', include('django.contrib.auth.urls')), # django default views
    path('accounts/users/', users, name='users'),
    path('accounts/user/', user, name='user'),
    path('accounts/add_to_cart/<pk>/', add_to_cart, name='add_to_cart'),
    path('accounts/update_item/<pk>/', ItemUpdateView.as_view(), name='update_item'),
    path('accounts/discard_item/<pk>/', discard_item, name='discard_item'),
    # path('accounts/delete_item/<pk>/', ItemDeleteView.as_view(), name='delete_item'),
    path('accounts/remove_item_from_cart/<pk>/', remove_item_from_cart, name='remove_item_from_cart'),
    path('accounts/your_cart/', your_cart, name='your_cart'),
    path('accounts/cart_confirm_delete/', cart_confirm_delete, name='cart_confirm_delete'),
    path('accounts/empty_cart/', empty_cart, name='empty_cart'),
    path('accounts/place_order/', place_order, name='place_order'),
    path('accounts/order_set_up/<pk>/', OrderUpdateView.as_view(), name='order_set_up'),
    path('accounts/order_preview/<pk>/', order_preview, name='order_preview'),
    path('accounts/order_confirmation/<pk>/', order_confirmation, name='order_confirmation'),
    path('accounts/order_decline/<pk>/', order_decline, name='order_decline'),
    path('accounts/order/<pk>/', order_summary, name='order_summary'),
    path('accounts/orders/', your_orders, name='your_orders'),
    path('accounts/all_orders/', OrdersListView.as_view(), name='all_orders'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/products/', api.views.Products.as_view()),
    path('api/product/<pk>/', api.views.ProductDetail.as_view()),
    path('api/categories/', api.views.Categories.as_view()),
    path('api/category/<pk>/', api.views.CategoryDetail.as_view()),
    path('api/users/', api.views.Users.as_view()),
    path('api/user/<pk>/', api.views.UserDetail.as_view()),
    path('api/user_products/', api.views.User_products.as_view()),
    path('api/user_product/<pk>/', api.views.User_productDetail.as_view()),
    path('api/profiles/', api.views.Profiles.as_view()),
    path('api/profile/<pk>/', api.views.ProfileDetail.as_view()),
    path('api/orders/', api.views.Orders.as_view()),
    path('api/order/<pk>/', api.views.OrderDetail.as_view()),
    path('api/order_products/', api.views.Order_products.as_view()),
    path('api/order_product/<pk>/', api.views.Order_productDetail.as_view()),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
