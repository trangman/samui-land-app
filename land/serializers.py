from rest_framework import serializers
from .models import Area, Property, Image, LandTitle

class LandTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandTitle
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    land_title = LandTitleSerializer(read_only=True)
    area_name = serializers.CharField(source='area.name', read_only=True)
    agency_name = serializers.CharField(source='agency.name', read_only=True)
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Property
        fields = '__all__'
