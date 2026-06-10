from django.shortcuts import render,redirect
from .models import Order, OrderItem
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from menu.models import MenuItem
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum


@staff_member_required
def all_orders_admin(request):

    users_data = []

    users = User.objects.filter(order__isnull=False).distinct()

    for user in users:

        orders = Order.objects.filter(user=user)

        total_orders = orders.count()

        total_payments = orders.aggregate(
            total=Sum('total_price')
        )['total'] or 0

        users_data.append({
            'user': user,
            'total_orders': total_orders,
            'total_payments': total_payments
        })

    return render(request, 'cart/all_orders.html', {
        'users_data': users_data
    })

@staff_member_required
def user_orders_admin(request, user_id):

    user = User.objects.get(id=user_id)

    orders = Order.objects.filter(user=user).order_by('-created_at')

    total_payments = orders.aggregate(
        total=Sum('total_price')
    )['total'] or 0

    return render(request, 'dashboard/user_orders.html', {
        'user_data': user,
        'orders': orders,
        'total_payments': total_payments
    })


@staff_member_required
def user_orders_admin(request, user_id):
    user = User.objects.get(id=user_id)
    orders = Order.objects.filter(user=user).order_by('created_at')

    return render(request, 'dashboard/users_order_history.html', {
        'user': user,
        'orders': orders
    })

# Create your views here.
@login_required
def cart(request):
    return render(request, "cart/mycart.html")

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at").prefetch_related("items__menu_item")

    data = []

    for order in orders:
        items = []

        for item in order.items.all():
            items.append({
                "name": item.menu_item.name,
                "quantity": item.quantity,
                "price": str(item.price),           # unit price
                "subtotal": str(item.subtotal),     # price × quantity
            })

        data.append({
            "id": order.id,
            "total_price": str(order.total_price),
            "created_at": order.created_at.isoformat(),
            "items": items
        })
    return JsonResponse({"orders": data})

@login_required
def order_history_page(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at").prefetch_related("items__menu_item")

    return render(request, "cart/order_history.html", {
        "orders": orders
    })


@login_required
def create_order(request):

    if request.method != "POST":
        return JsonResponse({
            "error": "Invalid request"
        }, status=400)

    try:

        data = json.loads(request.body)

        cart = data.get("cart", [])

        print("CART:", cart)

        if not cart:
            return JsonResponse({
                "error": "Cart is empty"
            }, status=400)

        total_price = 0

        order = Order.objects.create(
            user=request.user,
            total_price=0
        )

        for item in cart:

            item_id = item.get("id")

            if not item_id:
                return JsonResponse({
                    "error": "Missing item ID"
                }, status=400)

            menu_item = MenuItem.objects.get(id=item_id)

            quantity = int(item.get("quantity", 1))

            total_price += menu_item.price * quantity

            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=quantity,
                # price is set automatically in OrderItem.save()
            )

        order.total_price = total_price
        order.save()

        return JsonResponse({
            "message": "Order created successfully"
        })

    except MenuItem.DoesNotExist:

        return JsonResponse({
            "error": "Menu item not found"
        }, status=404)

    except Exception as e:

        print("ERROR:", str(e))

        return JsonResponse({
            "error": str(e)
        }, status=500)
    
