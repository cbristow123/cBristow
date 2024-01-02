from django.urls import path 
from . import views 
from .views import register

urlpatterns =[
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('products', views.products, name='products'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
]
