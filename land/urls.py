from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AreaViewSet, PropertyViewSet, ImageViewSet

router = DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
