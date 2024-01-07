from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Review

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['location', 'date_of_birth', 'website', 'bio', 'photo']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'description']
