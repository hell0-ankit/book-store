from django.shortcuts import render, redirect, get_object_or_404
from cart.models import Cart
from .models import Address, Order, OrderItem


def checkoutViews(request):

    cart = get_object_or_404(Cart, user=request.user)

    if request.method == "POST":

        address = Address.objects.create(
            user=request.user,
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            pincode=request.POST.get("pincode"),
        )

        order = Order.objects.create(
            user=request.user,
            address=address,
            total=cart.total,
        )

        for item in cart.items.all():

            OrderItem.objects.create(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.book.discount_price,
            )

        cart.items.all().delete()

        return redirect("orders:order_success")

    context = {
        "cart": cart,
        "cart_items": cart.items.all(),
        "total": cart.total,
    }

    return render(request, "orders/checkout.html", context)

def orderSuccessViews(request):
    return render(request, 'orders/order-success.html')
