from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from student.forms import StudentRegistrationForm, StudentLoginForm
from django.views.generic.edit import FormView
from student.models import Student
from django.urls import reverse_lazy

class StudentRegistrationView(FormView):
    template_name = 'generics/student/register.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('student:login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            #redirect('student/login')
            print(form)
        else:
            print(form.error)
        return super().form_valid(form)

class StudentLoginView(FormView):
    template_name = 'generics/student/login.html'
    form_class = StudentLoginForm
    success_url = reverse_lazy('college')
    
    def form_valid(self, form):
        #matric_number = form.cleaned_data.get('matric_number')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        #user = authenticate(request=self.request, matric_number=matric_number, password=password)
        user = authenticate(request=self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid matric number or password')
            return self.form_invalid(form)



def logout(request):
    return render(request, 'generics/student/signup.html')
