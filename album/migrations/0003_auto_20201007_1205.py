# Generated by Django 3.1.2 on 2020-10-07 10:05

import album.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20201003_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=album.models.random_filename),
        ),
    ]
