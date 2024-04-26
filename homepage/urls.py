from django.urls import path
from homepage import views as hpViews
from product import views as prViews

urlpatterns = [
    path('', hpViews.show_product, name="home"),
    path('car/<slug:slug>', prViews.car_details, name="car_detail"),
    path('accessary/<slug:slug>', prViews.accessary_details, name="accessary_detail"),
]
