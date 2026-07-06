from django.db import models
from django.conf import settings
from product.models import Book


class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cart" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @property
    def sub_total(self):
        return sum(item.subtotal for item in self.cartitem_set.all())

    def __str__(self):
        return f"{self.user}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items" )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("cart", "book")

    @property
    def sub_total_item(self):
        return self.quantity * self.book.discount_price
    

    def __str__(self):
        return f"{self.book.title} ({self.quantity})"