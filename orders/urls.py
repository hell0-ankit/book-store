from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkoutViews, name='checkout'),
    path('order-success/', views.orderSuccessViews, name='order_success'),
    
    ]