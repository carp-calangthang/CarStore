from django.shortcuts import render,  get_object_or_404
from django.http import HttpResponse
from .cart import Cart
from product.models import car_model, Accessary
from django.http import JsonResponse

def cart(request):
    cart_sumary = Cart(request)
    cart_car_product = cart_sumary.get_car_prods()
    cart_accesary_product = cart_sumary.get_accesary_prods()
    cart_quantity = cart_sumary.__car__len__() + cart_sumary.__accesary_len__()
    return render(request, 'cart.html', {"cart_car_product": cart_car_product, "cart_accesary_product": cart_accesary_product, "cart_quantity": cart_quantity})

def cart_add_car(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        car_product_id = int(request.POST.get('product_id'))
        car_product = get_object_or_404(car_model, id=car_product_id)

        cart.car_add(product=car_product)
        cart.session.save()  # Lưu giỏ hàng vào session

        cart_quantity = cart.__car__len__()

        response = JsonResponse({'qty: ': cart_quantity, 'Product Name: ': car_product.car_name})
        return response
    
def cart_delete_car(request):
    a = 1
    
def cart_update_car(request):
    a = 1
    
def cart_add_accesary(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        accesary_product_id = int(request.POST.get('accesary_product_id'))
        accesary_product = get_object_or_404(Accessary, id=accesary_product_id)

        cart.accesary_add(accesary_product=accesary_product)
        cart.session.save()  # Lưu giỏ hàng vào session

        cart_quantity = cart.__accesary_len__()

        response = JsonResponse({'qty: ': cart_quantity, 'Product Name: ': accesary_product.accessary_name})
        return response
