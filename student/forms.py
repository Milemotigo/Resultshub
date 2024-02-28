from django import forms
from student.models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'email', 'matric_number', 'address', 'bio', 'phone_number', 'birth_date', 'address', 'profile_picture']

