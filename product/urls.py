from product import views
from django.urls import path

urlpatterns = [
    path('product-listing/', views.productListing, name='product-listing'),
    path('product-detail/', views.productDetail, name='product-detail'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkOut, name='checkout'),
    path('order-success/', views.orderSuccess, name='order-success'),
]

