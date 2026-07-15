from django.shortcuts import render, get_object_or_404
from product.models import Book, Category, Author, Language, Publisher

def productListing(request):
    books = Book.objects.all()

    category = request.GET.get("category")
    author = request.GET.get("author")
    language = request.GET.get("language")
    publisher = request.GET.get("publisher")

    if category:
        books = books.filter(categories__slug=category)

    if author:
        books = books.filter(authors__slug=author)

    if publisher:
        books = books.filter(publisher__slug=publisher)

    if language:
        books = books.filter(language=language)

    books = books.distinct()

    context = {
        "books": books,
        "categories": Category.objects.all(),
        "authors": Author.objects.all(),
        "publishers": Publisher.objects.all(),   
        "language_choices": Language.choices,   
        "selected_category": category,
        "selected_author": author,
        "selected_publisher": publisher,
        "selected_language": language,
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
