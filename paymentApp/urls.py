from django.urls import path
from paymentApp import views

urlpatterns = [
    path('', views.payment, name="payment")
]
