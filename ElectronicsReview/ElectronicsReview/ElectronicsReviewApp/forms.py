from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Review, ContactSubmission

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

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'question']

class PasswordResetForm(forms.Form):
    username = forms.CharField(max_length=150)
    new_password1 = forms.CharField(widget=forms.PasswordInput)
    new_password2 = forms.CharField(widget=forms.PasswordInput)

    #username validation
    def clean_username(self):
        username = self.cleaned_data['username']
        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username does not exist.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('new_password1')
        password2 = cleaned_data.get('new_password2')

        #pw match validation
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data