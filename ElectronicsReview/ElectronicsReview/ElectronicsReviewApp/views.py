from django.shortcuts import render

def home (request):
    return render(request, 'ElectronicsReviewApp/home.html')

def about (request):
    return render(request, 'ElectronicsReviewApp/about.html')

def contact (request):
    return render(request, 'ElectronicsReviewApp/contact.html')

def products (request):
    return render(request, 'ElectronicsReviewApp/products.html')

def register (request):
    return render(request, 'ElectronicsReviewApp/register.html')

def login (request):
    return render(request, 'ElectronicsReviewApp/login.html')

