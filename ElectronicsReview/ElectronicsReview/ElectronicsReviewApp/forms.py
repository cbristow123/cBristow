""" https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms """

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'profile_pic']
