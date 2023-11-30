from django.urls import path, include

from product import views

urlpatterns = [
    path('all-products/', views.ProductsList.as_view()),
    path('products/<slug:category_slug>/', views.CategoryList.as_view()),
    path('favorites/', views.FavoritesList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view())
]