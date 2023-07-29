from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AreaViewSet, PropertyViewSet, ImageViewSet, PropertyByReferenceNumber

router = DefaultRouter()
router.register(r'areas', AreaViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'images', ImageViewSet)

urlpatterns = [
    path('properties/ref/<str:reference_number>/', PropertyByReferenceNumber.as_view()),
    path('', include(router.urls)),
]

