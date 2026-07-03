from product.models import Category, Author, Publisher

def book_categories(request):
    categories= Category.objects.all()
    return {
        "book_category": categories
    }

def book_author(request):
    author =Author.objects.all()
    return{
        "book_authors" : author
    }
def book_publisher(request):
    publisher = Publisher.objects.all()
    return{
        "book_publisher": publisher
    }