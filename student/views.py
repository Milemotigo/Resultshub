from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from student.forms import StudentRegistrationForm
from django.views.generic.edit import FormView
from generics.models import CustomUser
from django.urls import reverse_lazy

class StudentRegistrationView(FormView):
    template_name = 'generics/student/register.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('result:results')

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        else:
            print(form.error)
        return super().form_valid(form)

'''class StudentLoginView(FormView):
    template_name = 'generics/student/login.html'
    form_class = StudentLoginForm
    success_url = reverse_lazy('college')
    
    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = CustomUser.objects.get(email=email).first()
        if user:
            user = authenticate(email=email, password=password)
            if user is not None:
                login(self.request, user)
                return super().form_valid(form)
            else:
                form.add_error(None, 'Invalid matric number or password')
                print('not found')
                return self.form_invalid(form)
        else:
            form.add_error(None, 'Email does not exists ')
            return self.form_invalid(form)

'''
def logout(request):
    return render(request, 'generics/student/signup.html')
