from django.shortcuts import render, redirect
from product.filters import get_latest_books, get_top_discount_books, get_top_authors
from django.contrib import messages
from .models import NewsletterSubscriber

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
def privacyPolicy(request):
    return render(request, 'core/privacy_policy.html')
def faqView(request):
    return render(request, 'core/faq.html')

def contactViews(request):
    return render(request, 'core/contact.html')

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        
        if email:
            _, created = NewsletterSubscriber.objects.get_or_create(email=email)
            if created:
                messages.success(request, "Thank you for subscribing to our newsletter!")
            else:
                messages.info(request, "You are already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")

    # Redirect back to the page the user submitted from
    return redirect(request.META.get('HTTP_REFERER', '/'))