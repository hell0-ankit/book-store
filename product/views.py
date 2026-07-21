from django.shortcuts import render, get_object_or_404
from product.models import Book, Category, Author, Language, Publisher
from product.filters import filter_books

def productListing(request):
    books = filter_books(request)

    context = {
        "books": books,
        "categories": Category.objects.all(),
        "authors": Author.objects.all(),
        "publishers": Publisher.objects.all(),   
        "language_choices": Language.choices,   
    }
    return render(request, "product/product-listing.html", context)

def productDetail(request, slug):
    product_details = get_object_or_404(Book,slug=slug)
    context = {
        "book_detail": product_details,
    }
    return render(request, 'product/product-details.html', context)


def collection(request):

    return render(request, "product/collection.html")
