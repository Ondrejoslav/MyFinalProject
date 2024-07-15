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
from itertools import product

from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from accounts.views import *
from store.views import *
from store.forms import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('categories/', categories, name='categories'),
    path('category/<pk>/', category, name='category'),
    path('products/', products, name='products'),
    path('products_and_categories/', products_and_categories, name='products_and_categories'),
    path('product/<pk>/', product, name='product'),
    path('customer/create/', CustomerCreateView.as_view(), name='register_customer'),

    # path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/login/', SubmittableLoginView.as_view(), name='login'), # customized login view
    path('accounts/signup/', SignUpView.as_view(), name='signup'), # customized signup view
    # path('accounts/profile/', SignUpView.as_view(), name='profile'),
    path('accounts/users/', users, name='users'),
    path('accounts/user/<pk>/', user, name='user'),
    path('accounts/password_change/', SubmittablePasswordChangeView.as_view(), name='password_change'), # customized password change view
    path('accounts/', include('django.contrib.auth.urls')), # django default views
]
