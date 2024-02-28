from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from student.forms import StudentRegistrationForm
from django.views.generic.edit import FormView
from .models import CustomUser, Student
from django.urls import reverse_lazy

class UserFormView(FormView):
    template_name = 'generics/student/register.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('student:login')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            #redirect('student/login')
        else:
            print(form.error)
        return super().form_valid(form)

def login(request):
    return render(request, 'generics/student/login.html')
