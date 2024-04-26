from django.urls import path
from cart import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add-car/', views.cart_add_car, name="car_cart_add"),
    path('add-accesary/', views.cart_add_accesary, name="accesary_cart_add"),
    path('delete-car/', views.cart_delete_car, name="car_cart_delete"),
    path('update-car/', views.cart_update_car, name="car_cart_update"),
]
