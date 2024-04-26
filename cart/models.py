import uuid
from product.models import *
from django.db import models
from django.contrib.auth.models import User

class cart(models.Model):
    cart_uid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.cart_uid} - {self.user}"
    
class cart_car(models.Model):
    car_product  = models.ForeignKey(car_model, on_delete=models.CASCADE, related_name='car_items')
    cart = models.ForeignKey(cart, on_delete=models.CASCADE, related_name='cart_car_items')
    quantity = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.car_product.car_name} -  {self.cart.complete} - {self.car_product.car_price}"
    
class cart_accessary(models.Model):
    accessary_product  = models.ForeignKey(Accessary, on_delete=models.CASCADE, related_name='accessary_items')
    cart = models.ForeignKey(cart, on_delete=models.CASCADE, related_name='cart_accessary_items')
    quantity = models.IntegerField(default=0)
    date_add = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.accessary_product.accessary_name} -  {self.cart.complete} - {self.accessary_product.accessary_price}"