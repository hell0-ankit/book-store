from product.models import Category, Author, Publisher
from django.db.models import Count
def book_collections(request):
    return {
        "book_categories": Category.objects.annotate(
            categories_count=Count("books")
        ),
        "book_authors": Author.objects.annotate(
            author_count= Count("books")
        ),

        "book_publishers": Publisher.objects.annotate(
                    publishers_count= Count("books")
                ),
    }