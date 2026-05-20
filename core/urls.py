from core import views
from django.urls import path


urlpatterns = [
    path('home/', views.homeView, name='home'),
    path('', views.utilitesVeiws, name='utilites'),
]
