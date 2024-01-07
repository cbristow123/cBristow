from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Product, Profile, Review

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'price']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'date_of_birth', 'website']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'reviewer', 'rating', 'description']
