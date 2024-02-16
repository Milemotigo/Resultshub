from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from college.models import Department
from generics.models import CustomUser

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='college_staff')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff_id = models.IntegerField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Staffs', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    def __str__(self):
        return self.user.username
