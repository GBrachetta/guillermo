# Generated by Django 3.1.2 on 2020-11-05 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cd',
            name='out_of_stock',
            field=models.BooleanField(default=False),
        ),
    ]