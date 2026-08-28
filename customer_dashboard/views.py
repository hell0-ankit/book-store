from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum

from orders.models import Order
from .models import PersonalDetils
from .services import get_dashboard_data


@login_required
def customerDashboard(request):
    context = get_dashboard_data(request.user)
    return render(request, 'customer_dashboard/customer_dashboard.html', context)


@login_required
def cmOrdersHistory(request):
    all_orders = Order.objects.filter(user=request.user)
    orders_qs = all_orders.prefetch_related("items__book").order_by("-created_at")
    paginator = Paginator(orders_qs, 3)
    page_obj = paginator.get_page(request.GET.get("page"))

    total_spent = all_orders.exclude(
        status=Order.Status.CANCELLED
    ).aggregate(total=Sum("total"))["total"] or 0

    return render(request, 'customer_dashboard/cm_orders.html', {
        "total_orders": all_orders.count(),
        "active_orders": all_orders.filter(
            status__in=[Order.Status.PENDING, Order.Status.CONFIRMED, Order.Status.SHIPPED]
        ).count(),
        "total_spent": total_spent,
        "page_obj": page_obj,
        "orders": page_obj.object_list,
    })


@login_required
def cmPersonalDetails(request):
    context = get_dashboard_data(request.user)
    return render(request, 'customer_dashboard/cm_personal_details.html', context)


@login_required
def cmPersonalDetailsForm(request):
    if request.method == "POST":
        avatar = request.FILES.get('avatar')

        defaults = {
            "cm_phone": request.POST.get('phone'),
            "cm_gender": request.POST.get('gender'),
            "address": request.POST.get('address'),
        }

        dob = request.POST.get('dob')
        if dob:
            defaults["cm_dob"] = dob

        if avatar:
            defaults["profile_image"] = avatar

        PersonalDetils.objects.update_or_create(
            user_details=request.user,
            defaults=defaults
        )
        return redirect("cm_personal_details")

    context = get_dashboard_data(request.user)
    return render(request, 'customer_dashboard/update_personal_details.html', context)