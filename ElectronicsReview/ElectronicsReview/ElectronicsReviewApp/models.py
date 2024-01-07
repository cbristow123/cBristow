""" https://docs.djangoproject.com/en/5.0/topics/db/models/ """

""" 
I have fully removed the CustomUser class in this version. This is due to DB FK constraints that where caused
due to changing auth_type mid project. The documentation supporting this can be found here:
https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#changing-to-a-custom-user-model-mid-project
This meant a full Database rebuild, removing all migrations and starting a fresh. Old migrations can be found
at ElectronicsReviewApp/migrationsOLD
"""

from django.db import models
from django.contrib.auth.models import User  # Import User model
from django.dispatch import receiver
from django.db.models.signals import post_save

class Product(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    description = models.TextField(max_length=512)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_profile_picture(self):
        if self.photo:
            return self.photo.url
        else:
            return None

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Terrible'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    description = models.TextField(max_length=512)

    def __str__(self):
        return f"Review for {self.product.name} by {self.reviewer.user.username}"
