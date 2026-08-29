from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages
from cart.models import Cart
from .models import Address, Order, OrderItem


@login_required(login_url="login")
def checkoutViews(request):
    cart = get_object_or_404(Cart, user=request.user)

    if not cart.items.exists():
        messages.warning(request, "Your cart is empty.")
        return redirect("cart:cart")  
    if request.method == "POST":
        with transaction.atomic():
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
                unit_price = item.book.discount_price or item.book.price
                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price=unit_price,
                )

            cart.items.all().delete()

        return redirect("orders:order_success")

    context = {
        "cart": cart,
        "cart_items": cart.items.all(),
        "total": cart.total,
    }
    return render(request, "orders/checkout.html", context)


@login_required(login_url="login")
def orderSuccessViews(request):
    order = Order.objects.filter(user=request.user).order_by("-created_at").first()
    return render(request, "orders/order-success.html", {"order": order})

@login_required(login_url="login")
def download_invoice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    context = {
        'order': order,
        'items': order.items.all(),
    }
    return render(request, "orders/invoice.html", context)