from django.shortcuts import render
from product.filters import get_latest_books, get_top_discount_books

# Create your views here.
def homeView(request):
    
    context = {
        "latest_books":get_latest_books(),
        "top_discount_books": get_top_discount_books(),
    }
    return render(request, 'core/home.html', context)

def utilitesVeiws(request):
    return render(request, "utilites.html")
def aboutView(request):
    return render(request, 'core/about-us.html')