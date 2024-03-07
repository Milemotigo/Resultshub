from django.contrib.auth.backends import ModelBackend
from .models import Colleges


class collegeAuthBackend(ModelBackend):
    """College authentication backend file to handle login using username email and phone number"""
    
    def authenticate(self, request, username=None, password=None, **kwargs):
        # try:
        #     college = Colleges.objects.get(email=username)
        #     if college.check_password(password):
        #         return college
        # except Colleges.DoesNotExist:
        #     pass

        # try:
        #     college = Colleges.objects.get(username=username)
        #     if college.check_password(password):
        #         return college
        # except Colleges.DoesNotExist:
        #     pass
        
        # try:
        #     college = Colleges.objects.get(phone_number=username)
        #     if college.check_password(password):
        #         return college
        # except Colleges.DoesNotExist:
        #     return None
        try:
            user = Colleges.objects.get(email=username)
        except Colleges.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        
    
    def get_user(self, user_id):
        try:
            return Colleges.objects.get(pk=user_id)
        except Colleges.DoesNotExist:
            return None