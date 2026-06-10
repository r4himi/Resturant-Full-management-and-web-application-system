from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('users/<int:user_id>/orders/', views.users_orders_history, name='users_orders_history'),
]