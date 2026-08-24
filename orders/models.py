from django.conf import settings
from django.db import models
from product.models import Book


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.full_name
    class Meta:
        db_table = "user_address"
        verbose_name_plural = "Addresses"
        ordering = ["-created_at"]

class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "Pending", "Pending"
        CONFIRMED = "Confirmed", "Confirmed"
        SHIPPED = "Shipped", "Shipped"
        DELIVERED = "Delivered", "Delivered"
        CANCELLED = "Cancelled", "Cancelled"
    class PaymentStatus(models.TextChoices):
        UNPAID = "Unpaid", "Unpaid"
        PAID = "Paid", "Paid"
        FAILED = "Failed", "Failed"
        REFUNDED = "Refunded", "Refunded"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders")

    address = models.ForeignKey(
        Address, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )

    total = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    payment_status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.UNPAID,
        db_index=True
    )

    transaction_id = models.CharField(
        max_length=255, 
        blank=True, 
        null=True, 
        help_text="Gateway ID (e.g., Stripe, Razorpay)"
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
            db_table = "user_order"
            verbose_name_plural = "Orders"
            ordering = ["-created_at"]
            indexes = [
                models.Index(fields=["user", "-created_at"]),
            ]

    def __str__(self):
        return f"Order #{self.id} - {self.user} - {self.status}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price per unit at the time of purchase")

    @property
    def subtotal(self):
        return self.price * self.quantity
    class Meta:
        db_table = "book_order_item"
        verbose_name_plural = "Order Items"
    def __str__(self):
        return f"{self.quantity}x {self.book.title} (Order #{self.order.id})"