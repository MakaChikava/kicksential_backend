from django.shortcuts import render
from .serializers import ProductSerializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers

# Create your views here.
class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)