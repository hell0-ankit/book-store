from cart.models import Cart, CartItem

def cart_items(request):
    cart_items= CartItem.objects.all()
    cart_item = CartItem.objects.first()
    return {
        "cart_items": cart_items,
        "cart_item":cart_item
    }

def cart(request):
    total=Cart.objects.first()
    return{
        "total":total
        }
