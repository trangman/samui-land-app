# Generated by Django 4.1.7 on 2023-07-09 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0012_alter_property_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='land_size_acres',
            field=models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='land_size_sqf',
            field=models.DecimalField(blank=True, decimal_places=0, editable=False, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='land_size_sqm',
            field=models.DecimalField(blank=True, decimal_places=0, editable=False, max_digits=10, null=True),
        ),
    ]
