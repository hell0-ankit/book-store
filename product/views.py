from django.shortcuts import render

def productListing(request):
    return render(request, 'product/product-listing.html')

def productDetail(request):
    return render(request, 'product/product-details.html')


