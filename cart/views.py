from django.shortcuts import render

def cartViews(request):
    return render(request, 'cart/cart.html')