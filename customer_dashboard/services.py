from django.db.models import Sum
from orders.models import Order, OrderItem

def get_dashboard_data(user):
    orders = Order.objects.filter(user=user)

    return {
        "total_orders": orders.count(),

        "active_orders": orders.filter(
            status__in=[
                Order.Status.PENDING,
                Order.Status.CONFIRMED,
                Order.Status.SHIPPED,
            ]
        ).count(),

        "books_purchased": (
            OrderItem.objects.filter(order__user=user)
            .aggregate(total=Sum("quantity"))["total"] or 0
        ),

        "total_spent": (
            orders.aggregate(total=Sum("total"))["total"] or 0
        ),

        "recent_orders": orders.order_by("-created_at")[:5],
    }