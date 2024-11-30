from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.inventario.views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework_social_oauth2.urls')),
]
