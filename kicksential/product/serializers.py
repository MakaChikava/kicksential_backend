from rest_framework import serializers
from .models import Category, Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "name",
            "type",
            "get_absolute_url",
            "brand",
            "color",
            "price",
            "favorite",
            "image",
            
        )

class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializers(many=True)
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "products",
        )

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "name",
            "type",
            "get_absolute_url",
            "brand",
            "color",
            "price",
            "favorite",
            "image",
        )