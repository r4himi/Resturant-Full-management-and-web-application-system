from django.contrib import admin
from cart.models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

    fields = (
        "menu_item",
        "quantity",
        "price",
    )

    readonly_fields = ("price",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "total_price",
        "created_at",
    )

    inlines = [OrderItemInline]
