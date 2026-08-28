from django.db.models import Sum
from orders.models import Order, OrderItem
from .models import PersonalDetils


def get_dashboard_data(user):
    orders = Order.objects.filter(user=user)

    # 1. Recent 5 orders
    recent_orders = orders.prefetch_related("items__book").order_by("-created_at")[:5]

    # 2. Total spent: Only for PAID orders (excluding Cancelled/Failed/Unpaid)
    total_spent = orders.filter(
        payment_status=Order.PaymentStatus.PAID
    ).exclude(
        status=Order.Status.CANCELLED
    ).aggregate(total=Sum("total"))["total"] or 0

    # 3. Active orders count (In-progress pipeline)
    active_orders = orders.filter(
        status__in=[Order.Status.PENDING, Order.Status.CONFIRMED, Order.Status.SHIPPED]
    ).exclude(
        status=Order.Status.CANCELLED
    ).count()

    # 4. Books purchased: ONLY count books from PAID orders that are NOT cancelled
    books_purchased = OrderItem.objects.filter(
        order__user=user,
        order__payment_status=Order.PaymentStatus.PAID
    ).exclude(
        order__status=Order.Status.CANCELLED
    ).aggregate(total=Sum("quantity"))["total"] or 0

    # 5. User Profile
    profile = PersonalDetils.objects.filter(user_details=user).first()

    return {
        "total_orders": orders.count(),
        "active_orders": active_orders,
        "total_spent": total_spent,
        "books_purchased": books_purchased, 
        "recent_orders": recent_orders,
        "profile": profile,
    }