from django.shortcuts import render, redirect

def payment(request):
    return render(request, 'payment.html')