from django import forms
from .models import User, Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CustomPasswordChangeForm():
    pass

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']