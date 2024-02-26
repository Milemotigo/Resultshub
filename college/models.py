from django.db import models
from django.contrib.auth.models import User
# from generics.models import collegeUser, CustomUser
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser



class Colleges(AbstractUser):
    # Add your additional fields here
    college_name = models.CharField(max_length=250, unique=True, null=True)
    email = models.EmailField(max_length=150, unique=True)
    address = models.CharField(max_length=300, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Colleges', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    POBox_PMB = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date_founded = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField('auth.Group', related_name='collegeuser_set', blank=True)  
    user_permissions = models.ManyToManyField('auth.Permission', related_name='collegeuser_set', blank=True)  


class Department(models.Model):
    college = models.ForeignKey(Colleges, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=150, null=True)
    department_code = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return self.department_name


class Session(models.Model):
    session_name = models.CharField(max_length=100, unique=True, null=True)
    
    def __str__(self):
        return self.session_name


class Semester(models.Model):
    semester_name = models.CharField(max_length=10, unique=True, null=True)
    
    def __str__(self):
        return self.semester_name

