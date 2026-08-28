from django.shortcuts import render
from product.filters import get_latest_books, get_top_discount_books, get_top_authors

# Create your views here.
def homeView(request):
    
    context = {
        "latest_books":get_latest_books(),
        "top_discount_books": get_top_discount_books(),
        "top_authors": get_top_authors()
    }

    return render(request, 'core/home.html', context)

def aboutView(request):
    return render(request, 'core/about-us.html')