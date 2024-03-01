from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth import authenticate
from student.models import Student

class StudentRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Student
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    #email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': 'True', 'class': 'form-control'}))
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':'True', 'class':'form-control'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control'}))

