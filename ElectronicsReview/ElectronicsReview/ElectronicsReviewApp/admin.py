from django.contrib import admin
from .models import Product, CustomUser, Profile

# Register your models here.
admin.site.register(Product)
admin.site.register(Profile)

""" work in progress """

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    actions = ['custom_delete']

    def custom_delete(self, request, queryset):
        for user in queryset:
            try:
                profile = user.profile
                profile.delete()
            except Profile.DoesNotExist:
                pass  # No profile to delete

            user.delete()

    custom_delete.short_description = "Delete selected users and their profiles"










""" from django.contrib import admin
from .models import Product, CustomUser, Profile

admin.site.register(Product)
admin.site.register(CustomUser)
admin.site.register(Profile) """