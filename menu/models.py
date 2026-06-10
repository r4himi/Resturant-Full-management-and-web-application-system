from django.contrib.auth.models import User
from django.db import models
from decimal import Decimal

class MenuItem(models.Model):
    category = models.CharField(max_length=100)  
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
    upload_to='menu_images/',
    default='menu_images/default.jpg',
    blank=True
)
    is_vegetarian = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.category})"




# class OrderItem(models.Model):

#     order = models.ForeignKey(
#         Order,
#         on_delete=models.CASCADE,
#         related_name="items"
#     )

#     menu_item = models.ForeignKey(
#         MenuItem,
#         on_delete=models.CASCADE
#     )

#     quantity = models.PositiveIntegerField(default=1)

#     price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )

#     def __str__(self):
#         return f"{self.menu_item.name} x {self.quantity}"