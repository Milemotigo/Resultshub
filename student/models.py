from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from college.models import Department

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='college_student')
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    matric_number = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Students', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
