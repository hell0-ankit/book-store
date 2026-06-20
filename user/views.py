from django.shortcuts import render

# Create your views here.
def userPofile(request):
    return render(request, 'user/userprofile.html')
