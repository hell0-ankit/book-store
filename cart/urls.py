from django.urls import path
from . import views

# Namespacing define
app_name = 'cart' 

urlpatterns = [

    path('', views.cartViews, name='cart_detail'), 
]