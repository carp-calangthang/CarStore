from django.urls import path
from inventory import views

urlpatterns = [
    path('user-manager/', views.user_manager, name="user_manager"),
    path('product-manage/', views.product_manage, name="product_manager"),
    path('add_car_product/', views.add_car_product, name="add_car_product"),
    path('add_accessary_product/', views.add_accessary_product, name="add_accessary_product"),
]
