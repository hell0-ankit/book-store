from django.shortcuts import render, get_object_or_404
from product.models import Book

def productListing(request):
    products = Book.objects.all()
    context = {
    "books": products,
    }
    return render(request, 'product/product-listing.html', context)

def productDetail(request, slug):
    product_details = get_object_or_404(Book,slug=slug)
    context = {
        "book_detail": product_details,
    }
    return render(request, 'product/product-details.html', context)

# def category(request):

