from django.db.models import Q
from .models import Book
def filter_books(request):
    books = Book.objects.all()
    search = request.GET.get("search")
    category = request.GET.get("category")
    author = request.GET.get("author")
    publisher = request.GET.get("publisher")
    language = request.GET.get("language")

    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(authors__name__icontains=search) |
            Q(categories__name__icontains=search) |
            Q(publisher__name__icontains=search)|
            Q(language__icontains=search)
        )

    if category:
        books = books.filter(categories__slug=category)

    if author:
        books = books.filter(authors__slug=author)

    if publisher:
        books = books.filter(publisher__slug=publisher)

    if language:
        books = books.filter(language=language)

    return books.distinct()


def get_latest_books(limit=8):

    return Book.objects.order_by("-created_at")[:limit]

def get_top_discount_books(limit=8):
    return Book.objects.filter(
        discount_percentage__gt=0
    ).order_by("-discount_percentage", "-id")[:limit]