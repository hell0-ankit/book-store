from django.shortcuts import render

def productListing(request):
    return render(request, 'product/product-listing.html')

def productDetail(request):
    return render(request, 'product/product-details.html')

def cart(request):
    return render(request, 'product/cart.html')

def checkOut(request):
    return render(request, 'product/checkout.html')

def orderSuccess(request):
    return render(request, 'product/order-success.html')
