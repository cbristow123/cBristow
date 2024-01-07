""" https://docs.djangoproject.com/en/5.0/topics/http/views/ """
""" https://django-advanced-training.readthedocs.io/en/latest/features/class-based-views/ """

from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, ProfileForm, ReviewForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Product, Review, Profile
from django.contrib import messages
from django.views import View

def home(request):
    return render(request, 'ElectronicsReviewApp/home.html')

def about(request):
    return render(request, 'ElectronicsReviewApp/about.html')

def contact(request):
    return render(request, 'ElectronicsReviewApp/contact.html')

def products(request):   
    products = Product.objects.all()
    return render(request, 'ElectronicsReviewApp/products.html', {'products': products})

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

@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'ElectronicsReviewApp/edit_profile.html', {'form': form})

def view_reviews(request, product_id):
    product = Product.objects.get(id=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'ElectronicsReviewApp/view_reviews.html', {'product': product, 'reviews': reviews})

@login_required
def leave_reviews(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)

            # debugging to troubleshoot issues with correctly requesting user profs
            print("User Profile:", request.user.profile)

            review.reviewer = request.user.profile
            review.product = product
            review.save()
            return redirect('view_reviews', product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'ElectronicsReviewApp/leave_reviews.html', {'product': product, 'form': form})


def user_profile(request, user_profile_id):
    user_profile = get_object_or_404(Profile, id=user_profile_id)
    return render(request, 'ElectronicsReviewApp/user_profile.html', {'user_profile': user_profile})

def edit_review(request, product_id, review_id):
    product = get_object_or_404(Product, id=product_id)
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('view_reviews', product_id=product_id)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'ElectronicsReviewApp/edit_review.html', {'product': product, 'review': review, 'form': form})

def delete_review(request, product_id, review_id):
    product = get_object_or_404(Product, id=product_id)
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        review.delete()
        return redirect('view_reviews', product_id=product_id)

    return render(request, 'ElectronicsReviewApp/delete_review.html', {'product': product, 'review': review})

class ReviewDetailView(View):
    template_name = 'ElectronicsReviewApp/review_detail.html'

    def get(self, request, product_id, review_id):
        review = get_object_or_404(Review, product_id=product_id, id=review_id)
        return render(request, self.template_name, {'review': review})
