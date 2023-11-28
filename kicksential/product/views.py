from django.shortcuts import render
from .serializers import ProductSerializers

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers

# Create your views here.
