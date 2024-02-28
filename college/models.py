from django.db import models
from generics.models import collegeUser
from django.core.validators import FileExtensionValidator


class College(models.Model):
    user = models.OneToOneField(collegeUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Colleges', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])


class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=150)
    department_code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.department_name


class Session(models.Model):
    session_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.session_name


class Semester(models.Model):
    semester_name = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.semester_name

