from django.contrib import admin
from .models import College, Department, Student, Staff, Session, Semester, Result

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Result)
