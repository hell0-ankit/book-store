from django.contrib import admin
from django.utils.html import format_html
from .models import Address, Order, OrderItem


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "email", "phone", "city", "pincode", "address")
    search_fields = ("address",)
    ordering = ("-created_at",)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("book", "quantity", "get_formatted_price", "get_formatted_subtotal")
    fields = ("book", "quantity", "get_formatted_price", "get_formatted_subtotal")
    can_delete = False

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("book")

    @admin.display(description="Unit Price")
    def get_formatted_price(self, obj):
        if obj.price is None:
            return "—"
        return f"₹{obj.price:,.2f}"

    @admin.display(description="Subtotal")
    def get_formatted_subtotal(self, obj):
        if obj.price is None:
            return "—"
        return f"₹{obj.subtotal:,.2f}"


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id", "full_name", "email", "phone", "pincode", "city",
        "products_titles", "products_quantity",
        "colored_status", "colored_payment_status",
        "get_formatted_total", "created_at",
    )
    list_filter = ("status", "payment_status", "created_at", "address__city")
    search_fields = (
        "id", "user__username", "user__email", "transaction_id",
        "address__full_name", "address__email", "address__phone",
        "items__book__title",
    )
    readonly_fields = ("user", "address", "total", "transaction_id", "created_at", "updated_at")
    list_select_related = ("user", "address")
    raw_id_fields = ("user", "address")
    inlines = [OrderItemInline]

    fieldsets = (
        ("Order Overview", {
            "fields": ("user", "address", "status", "payment_status", "total", "transaction_id")
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("items__book")

    @admin.display(description="Name", ordering="address__full_name")
    def full_name(self, obj):
        return obj.address.full_name if obj.address else "—"

    @admin.display(description="Email", ordering="address__email")
    def email(self, obj):
        return obj.address.email if obj.address else "—"

    @admin.display(description="Phone", ordering="address__phone")
    def phone(self, obj):
        return obj.address.phone if obj.address else "—"

    @admin.display(description="Pincode", ordering="address__pincode")
    def pincode(self, obj):
        return obj.address.pincode if obj.address else "—"

    @admin.display(description="City", ordering="address__city")
    def city(self, obj):
        return obj.address.city if obj.address else "—"

    @admin.display(description="Product(s)")
    def products_titles(self, obj):
        titles = [item.book.title for item in obj.items.all()]
        return ", ".join(titles) if titles else "—"

    @admin.display(description="Quantity")
    def products_quantity(self, obj):
        items = obj.items.all()
        if not items:
            return "—"
        return ", ".join(str(item.quantity) for item in items)

    @admin.display(description="Total", ordering="total")
    def get_formatted_total(self, obj):
        if obj.total is None:
            return "—"
        return f"₹{obj.total:,.2f}"

    @admin.display(description="Order Status", ordering="status")
    def colored_status(self, obj):
        colors = {
            "Pending": "#E6A23C", "Confirmed": "#409EFF", "Shipped": "#909399",
            "Delivered": "#67C23A", "Cancelled": "#F56C6C",
        }
        color = colors.get(obj.status, "#000000")
        return format_html(
            '<span style="color: white; background-color: {}; padding: 4px 8px; border-radius: 4px; font-weight: bold;">{}</span>',
            color, obj.status,
        )

    @admin.display(description="Payment", ordering="payment_status")
    def colored_payment_status(self, obj):
        colors = {"Unpaid": "#F56C6C", "Paid": "#67C23A", "Failed": "#E6A23C", "Refunded": "#909399"}
        color = colors.get(obj.payment_status, "#000000")
        return format_html('<span style="color: {}; font-weight: bold;">{}</span>', color, obj.payment_status)