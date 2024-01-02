""" https://docs.djangoproject.com/en/5.0/topics/db/models/ """

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Product(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    description = models.TextField(max_length=512)
    photo = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.name
    
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='img/', blank=True, null=True)
    
    # Add related_name to avoid clashes with auth.User.groups
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    # Add related_name to avoid clashes with auth.User.user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
    
    def __str__(self):
        return self.username