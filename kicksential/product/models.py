# for image resizing
from io import BytesIO
from PIL import Image

# easier to create thumbnails
from django.core.files import File

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    slug = models.SlugField()
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    favorite = models.BooleanField(default=False)
    image = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='uploads/', blank=True, null=True) #upload_to is to folder called uploads bland and null true so that dont have to have images on all of the products
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    # def get_image(self):
    #     if self.image:
    #         return 'https://kicksentialbk-b4da2791ed28.herokuapp.com' + self.image.url
    #     return ''
    
    
    