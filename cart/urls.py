from django.urls import path
from . import views

# Namespacing define
app_name = 'cart' 

urlpatterns = [

    path("", views.cartDetail, name="cart"),
    path("add/<int:book_id>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<int:item_id>/", views.remove_to_cart, name="remove_to_cart"),
]