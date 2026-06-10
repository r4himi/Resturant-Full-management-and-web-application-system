from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name='profile'),
    path('delete/', views.delete_account, name = 'delete_account'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('users/', views.all_users_view, name='all_users'),
]