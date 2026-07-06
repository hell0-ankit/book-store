from cart.models import Cart, CartItem

def cart_items(request):
    cart_items= CartItem.objects.all()
    cart_item = CartItem.objects.first()
    return {
        "cart_items": cart_items,
        "cart_item":cart_item
    }

def cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return {
            "cart_total": cart.total,
            "cart": cart,
        }

    return {
        "cart_total": 0,
        "cart": None,
    }
