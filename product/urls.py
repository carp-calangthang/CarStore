from django.urls import path
from .views import *

urlpatterns = [
    path('car/', show_car, name="car"),
    path('accesary/', show_accesary, name="accesary"),
]
