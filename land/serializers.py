from rest_framework import serializers
from .models import Area, Property, Image

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = '__all__'
