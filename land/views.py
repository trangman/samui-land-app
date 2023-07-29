from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
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

class PropertyByReferenceNumber(APIView):
    def get_object(self, reference_number):
        try:
            return Property.objects.get(reference_number__iexact=reference_number)
        except Property.DoesNotExist:
            raise Http404

    def get(self, request, reference_number, format=None):
        property = self.get_object(reference_number)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
