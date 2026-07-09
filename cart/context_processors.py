from cart.models import Cart, CartItem
from django.db.models import Sum

def cart_items(request):
    cart_items= CartItem.objects.all()
    cart_item = CartItem.objects.first()
    if request.user.is_authenticated:
        total_quantity = (
            CartItem.objects.filter(cart__user=request.user)
            .aggregate(total=Sum("quantity"))["total"] or 0
        )
    else:
        total_quantity = 0
    print("count items : ", total_quantity)
    return {
        "cart_items": cart_items,
        "cart_item":cart_item,
        "total_quantity":total_quantity
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
