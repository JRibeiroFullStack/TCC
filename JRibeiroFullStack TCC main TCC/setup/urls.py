from django.contrib import admin
from django.urls import path, include
from sensores.views import SensorViewSet, PrevisaoiaViewSet, LogprevisaoiaViewSet, RegistrosinalViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sensorTipo', SensorViewSet, basename='sensores')
router.register('registro', RegistrosinalViewSet, basename='registros')
router.register('previsao', PrevisaoiaViewSet, basename='previsao')
router.register('logPrevisao', LogprevisaoiaViewSet, basename='logprevisao')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
