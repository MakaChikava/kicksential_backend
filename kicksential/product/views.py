from django.shortcuts import render
from .serializers import ProductSerializers
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductSerializers, CategorySerializer, FavoriteSerializer

# -----------GET ALL PRODUCTS ---------- #
class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    
# -----------GET CATEGORIES ----------#
class CategoryList(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
# -------------GET FAVORITES--------------- #
class FavoritesList(APIView):
    def get(self, request, format=None):
        favorites = Product.objects.filter(favorite = True)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)
    
# ---HANDLE GET, PUT, DELETE FOR EACH PRODUCT---- #
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializers