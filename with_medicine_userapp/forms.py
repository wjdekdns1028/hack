from django.contrib.auth import forms
from .models import CustomUser

class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'age', 'address']