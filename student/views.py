from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from student.forms import StudentRegistrationForm
from django.views.generic.edit import CreateView
from generics.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth import logout, login

class StudentRegistrationView(CreateView):
    template_name = 'generics/student/register.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('result:results')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Authenticate user
            user = form.get_user()
            # Login the user
            login(request, user)
            # Redirect to a success page
            return redirect('result:results')
    else:
        form = AuthenticationForm()
    return render(request, 'generics/student/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('student:login') 
