from django.urls import path, include

from product import views

urlpatterns = [
    path('all-products/', views.ProductsList.as_view()),
]