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
from student.serialized import ImageResizeMixin
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
    student = get_object_or_404(Student)
    return render(request, 'generics/student/dashboard.html' , {student: 'student'})

class StudentProfileView(View):
    '''student profile'''
    def get(self, request, user_id):
        student = get_object_or_404(Student, user_id=user_id)
        context = {'student':student}
        return render(request, 'generics/student/student_profile.html', context)

class StudentUpdateView(ImageResizeMixin, View):
    '''update student profile'''

    def get(self, request, user_id):
        student = get_object_or_404(Student, user_id=user_id)
        form = StudentProfileForm(instance=student)
        context = {
                'form':form,
                }
        return render(request, 'generics/student/student_update.html', context)

    def post(self, request, user_id):

        #imgPath = '../media/profile_picture/students'
        #avePath = '../media/profile_picture/students/resized'
        ##self.resizeImage(imgPath, savePath, width=200, height=200)

        student = Student.objects.get(user_id=user_id)
        form = StudentProfileForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations! Profile updated successfully.')
            return redirect('student:profile', user_id=user_id)
        else:
            messages.warning(request, 'Invalid input data.')
            return redirect('student:update', user_id=user_id)

def delete_student(request, user_id):
    '''delete a student'''
    student = get_object_or_404(Student, user_id=user_id)
    student.delete()
    return redirect('student:registration')

