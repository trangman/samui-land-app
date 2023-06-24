from django.db import models
from django.utils.crypto import get_random_string

class Area(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    # other fields as needed

class Property(models.Model):
    LAND_TITLES = [
        ('CHANOTE', 'Chanote'),
        ('NOR_SOR_SAM', 'Nor Sor Sam'),
        # add other options as needed
    ]

    ACCESS_TYPES = [
        ('CONCRETE_ROAD', 'Concrete Road'),
        ('DIRT_TRACK', 'Dirt Track'),
        ('OTHER', 'Other'),
        # add other options as needed
    ]

    WATER_OPTIONS = [
        ('YES', 'Yes'),
        ('NO', 'No'),
        # add other options as needed
    ]

    ELECTRICITY_OPTIONS = [
        ('YES', 'Yes'),
        ('NEARBY', 'Nearby'),
        ('NO', 'No'),
        # add other options as needed
    ]

    reference_number = models.CharField(max_length=10, unique=True)  # auto generated
    title = models.CharField(max_length=200)
    description = models.TextField()  # wysiwyg editor
    land_size_rai = models.DecimalField(max_digits=10, decimal_places=2)
    land_size_sqm = models.DecimalField(max_digits=10, decimal_places=2)  # converted from Rai
    land_title = models.CharField(max_length=20, choices=LAND_TITLES)
    price = models.DecimalField(max_digits=14, decimal_places=2)  # price in Thai baht
    access = models.CharField(max_length=20, choices=ACCESS_TYPES)
    water = models.CharField(max_length=10, choices=WATER_OPTIONS)
    electricity = models.CharField(max_length=10, choices=ELECTRICITY_OPTIONS)
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='properties')
    def save(self, *args, **kwargs):
        if not self.reference_number:
            # Generate a unique reference number
            self.reference_number = 'CS' + get_random_string(length=4, allowed_chars='0123456789')
        super().save(*args, **kwargs)

class Image(models.Model):
    image_url = models.URLField()  # URL of the image stored in Amazon S3 bucket
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='images')
