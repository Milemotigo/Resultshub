from django.db import models
from college.models import Department
from generics.models import CustomUser
from django.core.validators import FileExtensionValidator

class Student(CustomUser):
    #student_id = models.CharField(max_length=20, unique=True)
    #department = models.ForeignKey(Department, on_delete=models.CASCADE)
    matric_number = models.CharField(max_length=50, unique=True, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Students', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

