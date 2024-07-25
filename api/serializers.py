from rest_framework import serializers

from accounts.models import *
from store.models import Category, Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class User_productsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProduct
        fields = '__all__'


class User_productDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProduct
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class Order_productsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = '__all__'


class Order_productDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderProduct
        fields = '__all__'