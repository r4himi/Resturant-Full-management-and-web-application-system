from django.db import models
from django.contrib.auth.models import User  # ✅ IMPORTANT

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', null=True, blank=True, default="profile_images/default.jpg")

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class register(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=128)
    password2 = models.CharField(max_length=128)

    def __str__(self):
        return self.username

class login(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
