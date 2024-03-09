from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from generics.models import CustomUser
from student.models import Student

class StudentRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'phone_number', 'birth_date')  # Exclude confirm_password from fields
        placeholders = {
            'username': 'Username',
            'phone_number': 'Phone Number',
            'birth_date': 'Birth Date',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-md'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
        self.fields['password2'] = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class StudentChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = ('username', 'phone_number', 'birth_date')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control'}),
        }


class StudentLoginForm(forms.Form):

    username = forms.CharField(label='Username/Email', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=['first_name', 'last_name', 'matric_number', 'city', 'state', 'zipcode', 'profile_picture']
        # bootstrap classes
        widgets={
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'matric_number':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        #'phone':forms.NumberInput(attrs={'class':'form-control'}),
        'state':forms.Select(attrs={'class':'form-control'}),
        'zipcode':forms.TextInput(attrs={'class':'form-control'}),
        }
