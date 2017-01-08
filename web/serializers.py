from rest_framework import serializers

from .models import Product, SubCategories, Categories


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
