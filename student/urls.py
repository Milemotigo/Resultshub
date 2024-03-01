from django.urls import path
from student.views import StudentRegistrationView, logout
from student.forms import LoginForm
from django.contrib.auth import views as auth_view

app_name = 'student'

urlpatterns = [
    path('registration/', StudentRegistrationView.as_view(), name='registration'),
    #path('login/', StudentLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('login/', auth_view.LoginView.as_view(template_name='generics/student/login.html', authentication_form=LoginForm), name="login"),
]

