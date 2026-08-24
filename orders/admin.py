from django.contrib import admin
from django.utils.html import format_html
from .models import Address, Order, OrderItem


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "full_name",
        "user",
        "email",
        "phone",
        "city",
        "pincode",
        "created_at",
    )
    list_filter = ("city", "created_at")
    search_fields = ("full_name", "email", "phone", "city", "pincode", "user__username")
    ordering = ("-created_at",)
    
    # ⚡ Performance: Prevents extra SQL queries when loading user details
    list_select_related = ("user",)
    
    # ⚡ UX: Auto-completes user field instead of loading a giant dropdown menu
    raw_id_fields = ("user",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("book", "quantity", "get_formatted_price", "get_formatted_subtotal")
    fields = ("book", "quantity", "get_formatted_price", "get_formatted_subtotal")
    can_delete = False
    
    # ⚡ Performance: Joins Book table to inline query
    def get_queryset(self, request):
        return super().get_queryset(request).select_related("book")

    @admin.display(description="Unit Price")
    def get_formatted_price(self, obj):
        return f"₹{obj.price:,.2f}"

    @admin.display(description="Subtotal")
    def get_formatted_subtotal(self, obj):
        return f"₹{obj.subtotal:,.2f}"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user_link",
        "colored_status",
        "colored_payment_status",
        "get_formatted_total",
        "created_at",
    )
    list_filter = ("status", "payment_status", "created_at")
    search_fields = (
        "id",
        "user__username",
        "user__email",
        "transaction_id",
    )

    readonly_fields = (
        "user",
        "address",
        # "shipping_address_snapshot",
        "total",
        "transaction_id",
        "created_at",
        "updated_at",
    )

    # ⚡ Performance: Avoids N+1 query issue for user and address
    list_select_related = ("user", "address")
    
    # ⚡ UX: Searchable dropdowns for large user/address tables
    raw_id_fields = ("user", "address")

    inlines = [OrderItemInline]

    fieldsets = (
        ("Order Overview", {
            "fields": ("user", "status", "payment_status", "total", "transaction_id")
        }),
        
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    # --- Custom Displays ---

    @admin.display(description="User", ordering="user__username")
    def user_link(self, obj):
        return f"{obj.user.username} ({obj.user.email})"

    @admin.display(description="Total", ordering="total")
    def get_formatted_total(self, obj):
        return f"₹{obj.total:,.2f}"

    @admin.display(description="Order Status", ordering="status")
    def colored_status(self, obj):
        colors = {
            "Pending": "#E6A23C",     # Orange
            "Confirmed": "#409EFF",   # Blue
            "Shipped": "#909399",     # Gray
            "Delivered": "#67C23A",   # Green
            "Cancelled": "#F56C6C",   # Red
        }
        color = colors.get(obj.status, "#000000")
        return format_html(
            '<span style="color: white; background-color: {}; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color,
            obj.status,
        )

    @admin.display(description="Payment", ordering="payment_status")
    def colored_payment_status(self, obj):
        colors = {
            "Unpaid": "#F56C6C",   # Red
            "Paid": "#67C23A",     # Green
            "Failed": "#E6A23C",   # Orange
            "Refunded": "#909399", # Gray
        }
        color = colors.get(obj.payment_status, "#000000")
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.payment_status,
        )


# Removed OrderItemAdmin: Managed cleanly inside OrderAdmin via OrderItemInline