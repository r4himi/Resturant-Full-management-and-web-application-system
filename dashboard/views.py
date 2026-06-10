from datetime import timedelta
import json

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Order
from django.db.models import Sum
from django.utils.timezone import now
from django.contrib.auth.models import User
from cart.models import OrderItem

# Create your views here.
@login_required
def admin_dashboard(request):
    today = now().date()

    # --- Existing stats ---
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(total=Sum('total_price'))['total'] or 0
    top_customers = Order.objects.values('user__username').annotate(
        total_spent=Sum('total_price')
    ).order_by('-total_spent')[:5]

    # --- Trend calculation ---
    this_week_start = today - timedelta(days=7)
    last_week_start = today - timedelta(days=14)

    this_week_orders = Order.objects.filter(created_at__date__gte=this_week_start).count()
    last_week_orders = Order.objects.filter(
        created_at__date__gte=last_week_start,
        created_at__date__lt=this_week_start
    ).count()

    if last_week_orders == 0:
        orders_trend = 100 if this_week_orders > 0 else 0
    else:
        orders_trend = ((this_week_orders - last_week_orders) / last_week_orders) * 100

    # --- Last 7 days loop (shared labels) ---
    day_labels = []
    weekly_orders = []
    weekly_revenue = []
    weekly_customers = []

    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        day_labels.append(day.strftime("%a"))

        weekly_orders.append(
            Order.objects.filter(created_at__date=day).count()
        )
        weekly_revenue.append(float(
            Order.objects.filter(created_at__date=day)
            .aggregate(total=Sum('total_price'))['total'] or 0
        ))
        weekly_customers.append(
            User.objects.filter(date_joined__date=day).count()
        )

    # --- Top selling items ---
    top_items = (
    OrderItem.objects
    .values('menu_item__name')        # ← changed
    .annotate(total_sold=Sum('quantity'))
    .order_by('-total_sold')[:5]
    )
    item_labels = [i['menu_item__name'] for i in top_items]  # ← changed
    item_sales  = [i['total_sold'] for i in top_items]
    return render(request, "dashboard/admin_dashboard.html", {
        # existing
        "total_orders":   total_orders,
        "total_revenue":  total_revenue,
        "top_customers":  top_customers,
        "orders_trend":   orders_trend,

        # charts
        "chart_labels":      json.dumps(day_labels),
        "weekly_orders":     json.dumps(weekly_orders),
        "weekly_revenue":    json.dumps(weekly_revenue),
        "weekly_customers":  json.dumps(weekly_customers),
        "item_labels":       json.dumps(item_labels),
        "item_sales":        json.dumps(item_sales),
    })

def users_orders_history(request, user_id):
    orders = Order.objects.filter(user_id=user_id).order_by('-created_at')
    return render(request, "dashboard/users_order_history.html", {
        'user_id': user_id,
        'orders': orders
    })