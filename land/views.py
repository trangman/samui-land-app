from django.shortcuts import render
from rest_framework import viewsets
from .models import Area, Property, Image
from .serializers import AreaSerializer, PropertySerializer, ImageSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# Create your views here.
