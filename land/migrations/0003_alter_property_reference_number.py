# Generated by Django 4.1.7 on 2023-06-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0002_agency_property_agency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='reference_number',
            field=models.CharField(blank=True, max_length=10, unique=True),
        ),
    ]