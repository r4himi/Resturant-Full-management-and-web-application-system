from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('create-orders/', views.create_order, name='orders'),
    path('orders/', views.order_history_page, name='orders_page'),
    path("api/orders/", views.order_history, name="orders_api"),
    path('all-orders/', views.all_orders_admin, name='admin_all_orders'),
    path('users/<int:user_id>/orders/', views.user_orders_admin, name='user_orders_admin'),
    path('admin/user-orders/<int:user_id>/',views.user_orders_admin,name='user_orders_admin'),
]