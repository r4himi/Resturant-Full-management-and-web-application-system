from django.shortcuts import get_object_or_404, redirect, render
from .models import MenuItem
from collections import defaultdict
from .forms import MenuItemForm
from django.contrib.admin.views.decorators import staff_member_required
from django.core.mail import send_mail
from django.conf import settings

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject="New Contact Message",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        return redirect("contact")  # or any page you want

    # IMPORTANT: return something for GET request
    return render(request, "menu/contact.html")

#add item class which can add item to the menu
@staff_member_required
def add_item(request):
    if request.method == "POST":
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("menu")
    else:
        form = MenuItemForm()
    return render(request,  "menu/add_item.html", {"form": form})

#delete item class which can do a soft delete which means it deleted just from the view not database
@staff_member_required
def delete_item(request, id):
    item = get_object_or_404(MenuItem, id = id)

    if request.method == "POST":
        item.is_active = False
        item.save()
        return redirect('menu')
    return render(request, 'menu/confirm_delete.html', {'items': item})

#edit item class which you can update and edit the items
@staff_member_required
def edit_item(request, id):
    item = get_object_or_404(MenuItem, id=id)

    if request.method == "POST":
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('menu')
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'menu/edit.html', {'form':form})

        

def home(request):
    return render(request, "menu/index.html")

def about(request):
    return render(request, "menu/aboutus.html")

def contact(request):
    return render(request, "menu/contactus.html")

#menu class which show the menu items
def menu(request):
    items = MenuItem.objects.filter(is_active=True).order_by("category", "name")

    grouped_items = defaultdict(list)

    for item in items:
        category = item.category.strip().title()  
        grouped_items[category].append(item)

    context = {
        "grouped_items": dict(grouped_items)
    }

    return render(request, "menu/menu.html", context)

def reservation(request):
    return render(request, "menu/reservation.html")


