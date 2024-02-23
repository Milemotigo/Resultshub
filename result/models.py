from django.db import models
from student.models import Student
from college.models import (Session,
                              Department,
                              Semester,
                              )


# Create your models here.

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=100)
    course_title = models.CharField(max_length=100)
    course_unit = models.IntegerField()
    score = models.IntegerField()
    grade = models.CharField(max_length=5)
    level = models.IntegerField()
    remark = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.student} - {self.session} - Semester {self.semester} - {self.course_title} - Level {self.level} - {self.grade}'

class Token(models.Model):
    token_code = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('unused', 'Unused'), ('used', 'Used')], default='unused')
    date_purchased = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.token_code

