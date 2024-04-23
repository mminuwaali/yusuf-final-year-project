from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "email",
            "username",
            "password1",
            "password2",
            "last_name",
            "first_name",
        ]
