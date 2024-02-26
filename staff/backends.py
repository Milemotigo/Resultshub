from typing import Any
from django.contrib.auth.backends import ModelBackend
from .models import Staff


class collegeAuthBackend(ModelBackend):
    """College authentication backend file to handle login using username email and phone number"""
    # def authenticate(self, request: HttpRequest, username: str | None = ..., password: str | None = ..., **kwargs: Any) -> AbstractBaseUser | None:
    #     return super().authenticate(request, username, password, **kwargs)
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            staff = Staff.objects.get(email=username)
            if staff.check_password(password):
                return staff
        except Staff.DoesNotExist:
            pass

        try:
            staff = Staff.objects.get(username=username)
            if staff.check_password(password):
                return staff
        except Staff.DoesNotExist:
            pass
        
        try:
            staff = Staff.objects.get(phone_number=username)
            if staff.check_password(password):
                return staff
        except Staff.DoesNotExist:
            return None
        
    
    def get_user(self, user_id):
        try:
            return Staff.objects.get(pk=user_id)
        except Staff.DoesNotExist:
            return None