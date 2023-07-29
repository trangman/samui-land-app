# Generated by Django 4.1.7 on 2023-06-25 09:02

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0009_alter_property_land_size_ngan_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='latitude',
            field=models.DecimalField(decimal_places=10, default=0, editable=False, max_digits=10),
        ),
        migrations.AddField(
            model_name='property',
            name='longitude',
            field=models.DecimalField(decimal_places=10, default=0, editable=False, max_digits=10),
        ),
        migrations.AlterField(
            model_name='area',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]