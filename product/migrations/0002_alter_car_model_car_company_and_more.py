# Generated by Django 4.2.4 on 2023-12-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_model',
            name='car_company',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='car_information',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='car_model',
            name='car_name',
            field=models.CharField(max_length=50),
        ),
    ]
