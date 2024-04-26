from django.shortcuts import render
from product.models import *
from cart.context_processors import *

def show_product(request):

    is_admin = request.user.is_staff
    car_product = car_model.objects.all()
    accessary_product = Accessary.objects.all
    
    return render(request, "home.html", {'cart_quantity': cart_quantity(request)['cart_quantity'], 'cart': cart(request), "car": car_product, "is_admin": is_admin, 'accesary': accessary_product})
