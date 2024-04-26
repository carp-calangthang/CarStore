import os
import random
import string
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class car_model(models.Model):
    car_color_choice = (
        ("Red", "Red"),
        ("Green", "Green"),
        ("Yellow", "Yellow"),
        ("White", "White"),
        ("Black", "Black")
    )
    car_uid = models.CharField(max_length=10, null=False, unique=True, blank=True)
    car_name = models.CharField(max_length=50, null=False)
    car_company = models.CharField(max_length=50, null=False)
    car_price = models.FloatField(max_length=50, null=False, default=0)
    car_color = models.CharField(
        max_length=20,
        choices=car_color_choice,
        default="Red"
    )
    car_information = models.TextField(max_length=200, null=False)
    car_images = models.ImageField(upload_to='images/%y/%m/%d', default='https://t3.ftcdn.net/jpg/01/71/13/24/360_F_171132449_uK0OO5XHrjjaqx5JUbJOIoCC3GZP84Mt.jpg')
    car_quantity = models.IntegerField(default=1)
    car_year = models.CharField(max_length=4, null=False, default="")
    slug = models.SlugField(max_length=200, unique=True, null=False, blank=True, editable=False)
    upload_date  = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-upload_date',)
        
    def generate_car_uid(self):
        digits = ''.join(random.choices(string.digits, k=5))
        car_uid = digits
        return car_uid
    
    def __str__(self):
        return f"{self.car_name}  -  {self.car_company}"

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            self.slug = slugify(self.car_name)
            
        if not self.car_uid:
            self.car_uid = self.generate_car_uid()

        super(car_model, self).save(*args, **kwargs)
        
class Accessary(models.Model):
    accessary_uid = models.CharField(max_length=10, null=False, blank=True, editable=False)
    accessary_name = models.CharField(max_length=50, null=False, default="")
    accessary_company = models.CharField(max_length=50, null=False)
    accessary_price = models.FloatField(max_length=50, null=False)
    accessary_info = models.TextField(max_length=200, null=False)
    accessary_images = models.ImageField(upload_to='images/%y/%m/%d', default=None)
    accessary_quantity = models.IntegerField(default=1)
    slug = models.SlugField(max_length=50, unique=True, null=False, blank=True, editable=False)
    upload_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-upload_date',)
        
    def __str__(self):
        return f"{self.accessary_name} - {self.accessary_company}"
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    
    def generate_accessary_uid(self):
        digits = ''.join(random.choices(string.digits, k=5))
        car_uid = digits
        return car_uid

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == '':
            self.slug = slugify(self.accessary_name)
            
        if not self.accessary_uid:
            self.accessary_uid = self.generate_accessary_uid()

        super(Accessary, self).save(*args, **kwargs)
    