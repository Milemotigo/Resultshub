from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    '''form for student registration'''

    class Meta:
        model = Student
        fields = ['user', 'department', 'matric_number', 'profile_picture']
