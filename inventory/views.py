from django.shortcuts import render, redirect
from product.models import car_model, Accessary
from userApp.models import UserProfile, User
from inventory.forms import add_car_product_forms, add_accessary_product_forms

def user_manager(request):
    
    user_items = UserProfile.objects.all()
    
    return render(request, "manager.html",  {"profiles": user_items})

def product_manage(request):
    car_items = car_model.objects.all
    accessary_items = Accessary.objects.all()
    
    return render(request, "product_manage.html", {"car_items": car_items, "accessary_items": accessary_items})

def add_car_product(request):
    
    car_form = add_car_product_forms(request.POST)
    
    if request.method == "POST":
        car_form = add_car_product_forms(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect('/')
        else:
            print(car_form.errors)
            
    else:
        car_form = add_car_product_forms()
        print("request.get")
        
    return render(request, 'add_car_product.html', {'car_form': car_form})

def add_accessary_product(request):
    
    accessary_form = add_accessary_product_forms(request.POST)
    
    if request.method == "POST":
        accessary_form = add_accessary_product_forms(request.POST, request.FILES)
        if accessary_form.is_valid():
            accessary_form.save()
            return redirect('/')
        else:
            print(accessary_form.errors)
            
    else:
        accessary_form = add_accessary_product_forms()
        print("request.get")
        
    return render(request, 'add_accessary_product.html', {'accessary_form': accessary_form})