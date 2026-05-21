from django.shortcuts import render

# Create your views here.
def homeView(request):
    return render(request, 'core/home.html')
def utilitesVeiws(request):
    return render(request, "utilites.html")
def aboutView(request):
    return render(request, 'core/about-us.html')