from django.shortcuts import get_object_or_404, render, redirect
from product.models import Book
from cart.models import Cart, CartItem



from django.shortcuts import get_object_or_404, redirect

def add_to_cart(request, book_id):
    # Get the selected book
    book = get_object_or_404(Book, id=book_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the book already exists in the cart
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
    )

    # If book already exists, increase quantity
    quantity = int(request.POST.get("quantity", 1))
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
    )

    if item_created:
        cart_item.quantity = quantity
    else:
        cart_item.quantity += quantity

    cart_item.save()

    return redirect("cart:cart")

def cartDetail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    context = {
        "cart": cart,
        "cart_items": cart.items.all(),
    }
    return render(request, 'cart/cart.html', context)



def remove_to_cart(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart_item.delete()
    return redirect("cart:cart")