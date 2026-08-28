from django.shortcuts import get_object_or_404, render, redirect
from product.models import Book
from cart.models import Cart, CartItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    cart, _ = Cart.objects.get_or_create(user=request.user)

    quantity = int(request.POST.get("quantity", 1))

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book,
        defaults={"quantity": quantity}
    )

    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    messages.success(request, "Product added to cart.")
    return redirect("cart:cart")


@login_required(login_url="login")
def cartDetail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    context = {
        "cart": cart,
        "cart_items": cart.items.all(),
    }
    return render(request, 'cart/cart.html', context)


@login_required(login_url="login")
def remove_to_cart(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart_item.delete()
    return redirect("cart:cart")