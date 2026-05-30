from django.shortcuts import render

# Create your views here.
def loginViews(request):
    return render(request, 'accounts/login.html')