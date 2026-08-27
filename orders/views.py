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



from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from orders.models import Order




@login_required
def orderSuccessViews(request):
    all_orders = Order.objects.filter(user=request.user)

    orders_qs = all_orders.prefetch_related("items__book").order_by("-created_at")
    paginator = Paginator(orders_qs, 3)  # per page 3, screenshot jaisa
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, 'customer_dashboard/cm_orders.html', {
        "total_orders": all_orders.count(),
        "active_orders": all_orders.filter(
            status__in=[Order.Status.PENDING, Order.Status.CONFIRMED, Order.Status.SHIPPED]
        ).count(),
        "total_spent": all_orders.aggregate(total=Sum("total"))["total"] or 0,
        "page_obj": page_obj,
        "orders": page_obj.object_list,
    })