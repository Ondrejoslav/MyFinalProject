from rest_framework import serializers

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

