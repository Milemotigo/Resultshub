from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from student.forms import StudentRegistrationForm, StudentLoginForm, StudentProfileForm
from django.views.generic.edit import CreateView
from generics.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages

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
    '''Update the student'''
    def get(self, request):
        form = StudentProfileForm()
        return render(request, 'generics/student/student_profile.html', locals())

    def post(self, request):
        form = StudentProfileForm(request.POST)

        if form.is_valid():
            user = request.user

            student = Student.object.get('user')

            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.matric_number = form.cleaned_data['matric_number']
            student.city = form.cleaned_data['city']
            student.phone = form.cleaned_data['phone']
            student.state = form.cleaned_data['state']
            student.zipcode = form.cleaned_data['zipcode']

            student.save()
            messages.success(request, 'Congratulations profile updated successfully')

        else:
            messages.warning(request, 'Invalid input data')
            return redirect('student:dashboard')
        return render(request, 'generics/student/student_profile.html', locals())

