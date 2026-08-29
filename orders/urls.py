from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkoutViews, name='checkout'),
    path('order-success/', views.orderSuccessViews, name='order_success'),
    path('invoice/<int:order_id>/', views.download_invoice, name='download_invoice')
    ]