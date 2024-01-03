from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

def home(request):
    return render(request, 'ElectronicsReviewApp/home.html')

def about(request):
    return render(request, 'ElectronicsReviewApp/about.html')

def contact(request):
    return render(request, 'ElectronicsReviewApp/contact.html')

def products(request):
    return render(request, 'ElectronicsReviewApp/products.html')

def profile(request):
    return render(request, 'ElectronicsReviewApp/profile.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'ElectronicsReviewApp/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Use the default authenticate function without specifying a backend
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid credentials')
    else:
        form = AuthenticationForm()

    return render(request, 'ElectronicsReviewApp/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')




