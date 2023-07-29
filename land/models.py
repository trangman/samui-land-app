from django.db import models
from tinymce import models as tinymce_models
from django.utils.crypto import get_random_string
from decimal import Decimal
import requests
def property_image_upload_path(instance, filename):
    # This function is called when a new image is uploaded.
    # 'instance' is the Image or Property instance being saved,
    # 'filename' is the original name of the uploaded file.
    # This function should return a string that will be used as the new path for the uploaded file.
    if isinstance(instance, Property):
        return f'agencies/{instance.agency.id}/properties/{instance.reference_number}/{filename}'
    else:  # instance is an Image
        return f'agencies/{instance.property.agency.id}/properties/{instance.property.reference_number}/{filename}'


class Area(models.Model):
    name = models.CharField(max_length=200)
    description = tinymce_models.HTMLField(null=True, blank=True)
    def __str__(self):
        return self.name

class Agency(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    telephone = models.CharField(max_length=20)
    prefix = models.CharField(max_length=2)
    starting_point = models.IntegerField(default=1)
    def __str__(self):
        return self.name
    class Meta:
            verbose_name_plural = "Agencies"

class LandTitle(models.Model):
    title = models.CharField(max_length=200)
    description = tinymce_models.HTMLField(null=True, blank=True)
    def __str__(self):
        return self.title

class Property(models.Model):
    
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

    reference_number = models.CharField(max_length=10, unique=True, blank=True, editable=False)
    title            = models.CharField(max_length=200)
    featured_image   = models.ImageField(upload_to=property_image_upload_path)
    description      = tinymce_models.HTMLField(null=True, blank=True)
    land_title       = models.ForeignKey(LandTitle, on_delete=models.SET_NULL, null=True, related_name='properties')
    land_size_rai    = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    land_size_ngan   = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    land_size_wah    = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    land_size_sqm    = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, editable=False)  
    land_size_sqft   = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True, editable=False)
    land_size_acres  = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, editable=False)
    price_thb        = models.DecimalField(max_digits=14, decimal_places=0)  # price in Thai baht
    price_usd        = models.DecimalField(max_digits=10, decimal_places=0, editable=False, default=0)
    price_gbp        = models.DecimalField(max_digits=10, decimal_places=0, editable=False, default=0)  
    price_eur        = models.DecimalField(max_digits=10, decimal_places=0, editable=False, default=0)  
    access           = models.CharField(max_length=20, choices=ACCESS_TYPES)
    water            = models.CharField(max_length=10, choices=WATER_OPTIONS)
    electricity      = models.CharField(max_length=10, choices=ELECTRICITY_OPTIONS)
    area             = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='properties')
    agency           = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='properties')
    longitude        = models.DecimalField(max_digits=10, decimal_places=10, editable=False, default=0)
    latitude         = models.DecimalField(max_digits=10, decimal_places=10, editable=False, default=0)
    def __str__(self):
        return self.reference_number
    def save(self, *args, **kwargs):
        if self.price_thb and not (self.price_usd and self.price_gbp and self.price_eur):
            # Get conversion rates
            response = requests.get('https://api.exchangerate-api.com/v4/latest/THB')
            data = response.json()
            usd_rate = Decimal(data['rates']['USD'])
            gbp_rate = Decimal(data['rates']['GBP'])
            eur_rate = Decimal(data['rates']['EUR'])

            # Calculate prices
            self.price_usd = self.price_thb * usd_rate
            self.price_gbp = self.price_thb * gbp_rate
            self.price_eur = self.price_thb * eur_rate
        if not self.reference_number:
            # Generate a unique reference number
            self.reference_number = self.agency.prefix + str(self.agency.starting_point).zfill(4)
            self.agency.starting_point += 1
            self.agency.save()
        total_sqm = (self.land_size_rai * Decimal(1600)) + (self.land_size_ngan * Decimal(400)) + (self.land_size_wah * Decimal(4))
        self.land_size_sqm = total_sqm
        self.land_size_sqf = total_sqm * Decimal(10.764)
        self.land_size_acres = total_sqm * Decimal(0.000247105)
        super().save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Properties"

class Image(models.Model):
    image_url = models.ImageField(upload_to=property_image_upload_path)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    