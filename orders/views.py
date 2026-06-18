from django.shortcuts import render

def checkoutViews(request):
    return render(request, 'orders/checkout.html')

def orderSuccessViews(request):
    return render(request, 'orders/order-success.html')
