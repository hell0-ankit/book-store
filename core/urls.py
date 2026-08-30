from core import views
from django.urls import path


urlpatterns = [
    path('', views.homeView, name='home'),
    path('about-us/', views.aboutView, name='about-us'),
    path("subscribe/", views.subscribe_newsletter, name="subscribe_newsletter"),
]
