from product import views
from django.urls import path

urlpatterns = [
    path('product-listing/', views.productListing, name='product-listing'),
    path('product-detail/<slug:slug>/', views.productDetail, name='product-detail'), 
]

