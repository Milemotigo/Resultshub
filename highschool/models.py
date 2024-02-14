from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class HighSchool(models.Model):
    name = models.CharField(max_length=250, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20, unique=True)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='highschool_staff')
    email = models.EmailField(max_length=254, unique=True)
    highschool = models.ForeignKey(HighSchool, on_delete=models.CASCADE)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff_id = models.IntegerField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Staffs', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
    def __str__(self):
        return self.user.username
    

class SSClass(models.Model):
    class_name = models.CharField(max_length=100, unique=True)
    class_code = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.class_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='highschool_student')
    email = models.EmailField(max_length=254, unique=True)
    # department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Students', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
   

class Result(models.Model):
    """"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_unit = models.IntegerField()
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    semester = models.CharField(max_length=10)
    session = models.CharField(max_length=10)
    level = models.IntegerField()
    remark = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.student} {self.course_code} {self.course_title} {self.course_unit} {self.score} {self.grade} {self.semester} {self.session} {self.level} {self.remark} {self.date}'


