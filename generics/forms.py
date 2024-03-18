from django import forms
from django.contrib.auth.forms import UserCreationForm
from college.models import Colleges


class collegeSignUpForm(UserCreationForm):
    """"""
    class Meta:
        model = Colleges
        fields = ('college_name', 'username', 'email', 'password1', 'password2',)

        