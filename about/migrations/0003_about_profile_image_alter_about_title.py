# Generated by Django 4.2.15 on 2024-09-02 22:52

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
