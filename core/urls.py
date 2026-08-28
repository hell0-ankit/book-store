from core import views
from django.urls import path


urlpatterns = [
    path('', views.homeView, name='home'),
    path('about-us/', views.aboutView, name='about-us'),
]
