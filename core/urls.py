from core import views
from django.urls import path


urlpatterns = [
    path('', views.homeView, name='home'),
    path('about-us/', views.aboutView, name='about-us'),
    path('privacy_policy/', views.privacyPolicy, name='privacy_policy'),
    path('faq', views.faqView, name='faq'),
    path('contact', views.contactViews, name='contact'),
    path("subscribe/", views.subscribe_newsletter, name="subscribe_newsletter"),
]
