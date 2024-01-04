from django.urls import path 
from . import views 
from .views import register, login_view, logout_view, edit_profile
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('profile', views.profile, name='profile'),
    path('logout', logout_view, name='logout'),
    path('profile/edit', edit_profile, name='edit_profile'),
]

