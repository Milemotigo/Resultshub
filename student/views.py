from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from student.forms import StudentRegistrationForm, StudentLoginForm, StudentProfileForm
from django.views.generic.edit import CreateView
from generics.models import CustomUser
from django.urls import reverse_lazy
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
    user = CustomUser.objects.all()
    return render(request, 'generics/student/dashboard.html' , {user: 'user'})

class StudentProfileView(View):
    '''student profile'''
    def get(self, request):
        #form = StudentProfileForm()
        student = Student.objects.all()
        for st in student:
            print(st.first_name)
        context = {'student':student}
        return render(request, 'generics/student/student_profile.html', context)

class StudentUpdateView(View):
    '''Update the student'''
    def get(self, request):
        form = StudentProfileForm()
        return render(request, 'generics/student/student_update.html', locals())
    def post(self, request):
        form = StudentProfileForm(request.POST)

        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            matric_number = form.cleaned_data['matric_number']
            city = form.cleaned_data['city']
            #student.phone = form.cleaned_data['phone']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']

            student = Student(
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    matric_number=matric_number,
                    city=city,
                    state=state,
                    zipcode=zipcode
                    )

            student.save()
            print(student.first_name)
            messages.success(request, 'Congratulations profile updated successfully')
            return redirect('student:profile')

        else:
            messages.warning(request, 'Invalid input data')
            return redirect('student:update')
        return render(request, 'generics/student/student_update.html', locals())

