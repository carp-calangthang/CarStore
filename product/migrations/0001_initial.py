# Generated by Django 4.2.4 on 2023-12-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.TextField(max_length=50)),
                ('car_company', models.TextField(max_length=50)),
                ('car_color', models.CharField(choices=[('Red', 'Red'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('White', 'White'), ('Black', 'Black')], default='Red', max_length=20)),
                ('car_information', models.CharField(max_length=200)),
                ('car_images', models.ImageField(default=None, upload_to='images/%y/%m/%d')),
                ('car_mini_image', models.ImageField(blank=True, default=None, null=True, upload_to='images/mini/%y/%m/%d')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-upload_date',),
            },
        ),
    ]
