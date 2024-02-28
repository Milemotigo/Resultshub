from django.db import models
from college.models import Department
from generics.models import CustomUser
from django.core.validators import FileExtensionValidator

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='college_student')
    password = models.CharField(max_length=120, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    matric_number = models.CharField(max_length=50, unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Students', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])

