from django.contrib.auth.backends import BaseBackend
from student.models import Student

class MatnumberAuthBackend(BaseBackend):
    def authenticate(self, matric_number=None, password=None):
        try:
            user = Student.objects.get('matric_number=matric_number')
            return user
        except Student.DoesNotExist:
            return None

