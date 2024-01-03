""" https://docs.djangoproject.com/en/5.0/topics/auth/customizing/ """
""" it was attempted to use both auth models simultaneously, however in the end, I just changed it to the custom model only """


from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CustomUserModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # Try to authenticate with the custom user model
        try:
            user = UserModel.objects.get_by_natural_key(username)
        except UserModel.DoesNotExist:
            user = None

        # If not found, try with the default user model (this is old and not used, leaving in to show mindset)
        if user is None:
            try:
                user = UserModel._default_manager.get_by_natural_key(username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user

        return None
