from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class College(models.Model):
    name = models.CharField(max_length=300, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=20, unique=True)


class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=150)
    department_code = models.CharField(max_length=20)
    
    def __str__(self):
        return self.department_name
    

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    student_id = models.IntegerField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Students', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    staff_id = models.IntegerField(unique=True)
    profile_picture = models.ImageField(upload_to='profile_picture/Staffs', default='default_user_icon.png', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    
    def __str__(self):
        return self.user.username


class Session(models.Model):
    session_name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.session_name


class Semester(models.Model):
    semester_name = models.CharField(max_length=10, unique=True)
    
    def __str__(self):
        return self.semester_name


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_unit = models.IntegerField()
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    level = models.IntegerField()
    remark = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.student} - {self.session} - Semester {self.semester} - {self.course_title} - Level {self.level} - {self.grade}'
