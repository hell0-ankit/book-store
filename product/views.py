from django.shortcuts import render, get_object_or_404
from product.models import Book

def productListing(request):
    products = Book.objects.all()
    return render(request, 'product/product-listing.html', {'books': products})

def productDetail(request, slug):
    product_details = get_object_or_404(Book,slug=slug)
    return render(request, 'product/product-details.html', {'book_details': product_details})


