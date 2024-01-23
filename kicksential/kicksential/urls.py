from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', TokenCreateView.as_view(), name='token_create'),  # Include JWT token creation view
    path('api/v1/', TokenDestroyView.as_view(), name='token_destroy'),  # Include JWT token destruction view
    path('api/v1/', include('product.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
