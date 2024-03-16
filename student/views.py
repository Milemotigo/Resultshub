from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from student.forms import StudentRegistrationForm, StudentLoginForm, StudentProfileForm
from django.views.generic.edit import CreateView
from generics.models import CustomUser
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages
from student.models import Student
from django.http import HttpResponseForbidden

class StudentRegistrationView(CreateView):
    template_name = 'generics/student/register.html'
    form_class = StudentRegistrationForm
    success_url = reverse_lazy('student:login')

'''def login_view(request):
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
'''

def login_view(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student:dashboard')
            else:
                error_message = 'username or password does not exist'
                return render(request, 'generics/student/login.html', {'form': form})
    else:
        form = StudentLoginForm()
    return render(request, 'generics/student/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('student:login')

@login_required
def dasboard_view(request):
    student = Student.objects.all()
    return render(request, 'generics/student/dashboard.html' , {student: 'student'})

class StudentProfileView(View):
    '''student profile'''
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        context = {'student':student}
        return render(request, 'generics/student/student_profile.html', context)

class StudentUpdateView(View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentProfileForm(instance=student)
        context = {
                'form':form,
                'student_id':id
                }
        return render(request, 'generics/student/student_update.html', context)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        form = StudentProfileForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Profile updated successfully.')
            return redirect('student:profile', id=id)
        else:
            messages.warning(request, 'Invalid input data.')
            return redirect('student:update', id=id)

"""
class StudentUpdateView(View):
    template_name = 'generics/student/student_update.
html'
    def post(request, id):
        student = Student.objects.get(id=id)

        f_name = request.POST['first_name']
        l_name = request.POST['last_name']

        student.first_name = f_name
        student.last_name = l_name
        student.save()
        return redirect('student:update')

"""

