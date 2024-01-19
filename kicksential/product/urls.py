from django.urls import path, include

from product import views

urlpatterns = [
    path('all-products/', views.ProductsList.as_view()),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/', views.CategoryList.as_view()),
    path('favorites/', views.FavoritesList.as_view()), # require authentification
    path('black/', views.getBlack.as_view()),
    path('red/', views.getRed.as_view()),
    path('green/', views.getGreen.as_view()),
    path('blue/', views.getBlue.as_view()),
    path('yellow/', views.getYellow.as_view()),
    path('pink/', views.getPink.as_view()),
    path('grey/', views.getGrey.as_view()),
    path('white/', views.getWhite.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view())
]