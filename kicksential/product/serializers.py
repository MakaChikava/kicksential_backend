from rest_framework import serializers
from .models import Category, Product

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "brand",
            "color",
            "price",
            "favorite",
            "get_image",
            
        )