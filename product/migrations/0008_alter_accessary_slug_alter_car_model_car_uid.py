# Generated by Django 4.2.4 on 2023-12-06 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_car_model_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessary',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='car_uid',
            field=models.CharField(default='', max_length=10, unique=True),
        ),
    ]