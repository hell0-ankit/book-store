from product.models import Category

def book_categories(request):
    categories= Category.objects.all()
    return {
        "book_category": categories
    }