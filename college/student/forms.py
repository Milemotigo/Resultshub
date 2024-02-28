from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    '''form for student registration'''
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    class Meta:
        model = Student
        fields = ['user', 'department', 'matric_number', 'profile_picture', 'first_name', 'last_name', 'password']
