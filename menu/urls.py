from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                # Home page
    path('about/', views.about, name='about'),        # About Us page
    path('contact/', views.contact, name='contact'),  # Contact Us page
    path('menu/', views.menu, name='menu'),           # Menu page
    path('reservation/', views.reservation, name='reservation'),  # Reservation page       
    path('add/', views.add_item, name = 'add'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('contact/send/', views.contact_view, name='contact_send'),
]
