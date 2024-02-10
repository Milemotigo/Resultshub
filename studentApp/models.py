from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class Department(models.Model):
    department_name = models.CharField(max_length=100, unique=True)
    department_code = models.CharField(max_length=10, unique=True)
    def __str__(self):
        return self.department_name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
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


