from django.db.models import Sum
from orders.models import Order, OrderItem
from .models import PersonalDetils


def get_dashboard_data(user):
    orders = Order.objects.filter(user=user)

    recent_orders = orders.prefetch_related("items__book").order_by("-created_at")[:5]

    total_spent = orders.exclude(
        status=Order.Status.CANCELLED
    ).aggregate(total=Sum("total"))["total"] or 0

    active_orders = orders.filter(
        status__in=[Order.Status.PENDING, Order.Status.CONFIRMED, Order.Status.SHIPPED]
    ).count()

    books_purchased = OrderItem.objects.filter(
        order__user=user
    ).exclude(
        order__status=Order.Status.CANCELLED
    ).aggregate(total=Sum("quantity"))["total"] or 0

    profile = PersonalDetils.objects.filter(user_details=user).first()

    return {
        "total_orders": orders.count(),
        "active_orders": active_orders,
        "total_spent": total_spent,
        "books_purchased": books_purchased,
        "recent_orders": recent_orders,
        "profile": profile,
    }