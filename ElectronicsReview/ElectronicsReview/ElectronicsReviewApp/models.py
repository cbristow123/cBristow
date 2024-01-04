""" https://docs.djangoproject.com/en/5.0/topics/db/models/ """

from django.db import models
from django.contrib.auth.models import AbstractUser
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
    
""" Custom User Model, to support use of a profile picture and experimentation """
class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='img/', blank=True, null=True)
    
    # Add related_name to avoid clashes with auth.User.groups
    groups = models.ManyToManyField(
    'auth.Group',
    related_name='customuser_groups',
    blank=True,
    verbose_name='groups',
    help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    
    # Add related_name to avoid clashes with auth.User.user_permissions
    user_permissions = models.ManyToManyField(
    'auth.Permission',
    related_name='customuser_permissions',
    blank=True,
    verbose_name='user permissions',
    help_text='Specific permissions for this user.',
    )
    
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
       return f"Profile for {self.user.username}"

""" 
Moved signals to signals.py

# Signal to create a profile upon user creation
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Signal to save the user profile
@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save() """

""" 
caused startup issues, so removed, this was exploring functionality of multiple auth models """  

""" class DefaultUserProxy(User):
    class Meta:
        proxy = True """
