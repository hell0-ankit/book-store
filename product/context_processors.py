from product.models import Category, Author, Publisher

def book_filters(request):
    return {
        "book_categories": Category.objects.all(),
        "book_authors": Author.objects.all(),
        "book_publishers": Publisher.objects.all(),
    }