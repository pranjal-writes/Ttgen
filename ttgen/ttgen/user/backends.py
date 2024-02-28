from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password  # Import check_password
from .models import CustomUser

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, user_id=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(user_id=user_id)
        except CustomUser.DoesNotExist:
            print('user not found')
            return None

        if user and check_password(password, user.password):
            print('success')
            return user
        prinf('failed')
        return None
