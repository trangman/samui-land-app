# Generated by Django 4.1.7 on 2023-06-24 10:00

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0004_alter_property_land_size_rai_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'verbose_name_plural': 'Agencies'},
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/land/'),
        ),
        migrations.AlterField(
            model_name='property',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
