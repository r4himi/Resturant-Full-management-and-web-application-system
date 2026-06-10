from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .models import Profile
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required



@staff_member_required
def all_users_view(request):
    users = User.objects.values('id','username', 'email', 'date_joined').order_by('username', 'id')
    return render(request, 'accounts/all_users.html', {'users': users})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    errors = {}

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if User.objects.filter(username=username).exists():
            errors['username'] = "Username already exists."

        if password1 != password2:
            errors['password2'] = "Passwords do not match."

        if not errors:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )

            messages.success(request, "Account created successfully!")
            return redirect('login')

    return render(request, "accounts/register.html", {'errors': errors})

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=profile)

    return render(request, "accounts/profile.html", {
        'u_form': u_form,
        'p_form': p_form,
        'profile': profile
    })


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully!")
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, "accounts/change_password.html", {
        'form': form
    })


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect('home')

    return render(request, "accounts/delete_account.html")


