from django.db import models
from menu.models import MenuItem
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def update_total(self):

        total = sum(
            item.price * item.quantity
            for item in self.items.all()
        )

        self.total_price = total
        self.save()

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        # store unit price (not multiplied by quantity)
        self.price = self.menu_item.price

        super().save(*args, **kwargs)

        # auto update order total
        self.order.update_total()

    @property
    def subtotal(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"