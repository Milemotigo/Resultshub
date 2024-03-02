from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from student.forms import StudentRegistrationForm, StudentChangeForm
from generics.models import CustomUser

class StudentAdmin(UserAdmin):
    add_form = StudentRegistrationForm
    form = StudentChangeForm
    model = CustomUser
    list_display = ['username', 'phone_number', 'birth_date']
    fieldsets = UserAdmin.fieldsets + (                                     (None, {'fields': ('phone_number', 'birth_date')}),
    ) #this will allow to change these fields in admin module


admin.site.register(CustomUser, StudentAdmin)
