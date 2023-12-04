from django.db.models import Q
from django.http import Http404


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

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

# ----------------- SEARCH ------------ #

@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(type__icontains= query) | Q(color__icontains= query)| Q(brand__icontains= query))
        serializer = ProductSerializers(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products", []})
    

# ----------------- COLOR -------------- #
# put Q in filter because model is a string because there is no ArrayField. Q can search and find the appropriate color 
class getBlack(APIView):
    def get(self, request, format=None,):
        color = Product.objects.filter(Q(color__icontains= 'black'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)
class getRed(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'red'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)
class getGreen(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'green'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)
class getYellow(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'yellow'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)
class getPink(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'pink'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)
    
class getBlue(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'blue'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)
    
class getGrey(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'grey'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)

class getWhite(APIView):
    def get(self, request, format=None):
        color = Product.objects.filter(Q(color__icontains= 'white'))
        serializer = FavoriteSerializer(color, many=True)
        return Response(serializer.data)