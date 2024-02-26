from django.contrib import admin
from college.models import (Colleges,
                            Department,
                            Session,
                            Semester
                            )
from student.models import Student
from staff.models import Staff
from result.models import Result


admin.site.register(Colleges)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Result)
