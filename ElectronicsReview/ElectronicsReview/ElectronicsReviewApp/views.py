from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def home(request):
    return render(request, 'ElectronicsReviewApp/home.html')

def about(request):
    return render(request, 'ElectronicsReviewApp/about.html')

def contact(request):
    return render(request, 'ElectronicsReviewApp/contact.html')

def products(request):
    return render(request, 'ElectronicsReviewApp/products.html')

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
    return render(request, 'ElectronicsReviewApp/login.html')
