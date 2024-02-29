from django import forms
from student.models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'email', 'password', 'matric_number', 'address', 'phone_number', 'birth_date', 'address', 'profile_picture']

class StudentLoginForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']
