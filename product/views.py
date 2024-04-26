from django.shortcuts import render, redirect, get_object_or_404
from cart.context_processors import *
from product.models import *

def show_car(request):
    car_product = car_model.objects.all
    return render(request, "car_list.html", {'cart_quantity': cart_quantity(request)['cart_quantity'], 'cart': cart(request), "car": car_product,})

def show_accesary(request):
    accessary_product = Accessary.objects.all
    return render(request, "accesary_list.html", {'cart_quantity': cart_quantity(request)['cart_quantity'], 'cart': cart(request), 'accesary': accessary_product})

def car_details(request, slug):
    
    car_product = get_object_or_404(car_model, slug=slug)
    
    return render(request, "car_details.html", {'cart_quantity': cart_quantity(request)['cart_quantity'], 'cart': cart(request), 'car_detail': car_product})

def accessary_details(request, slug):
    
    accessary_product = get_object_or_404(Accessary, slug=slug)
    
    return render(request, "accessary_details.html", {'cart_quantity': cart_quantity(request)['cart_quantity'], 'cart': cart(request), 'accessary_detail': accessary_product})