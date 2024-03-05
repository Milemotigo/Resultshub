from django.urls import path
from student.views import StudentRegistrationView, login_view, logout_view, dasboard_view

app_name = 'student'

urlpatterns = [
    path('registration/', StudentRegistrationView.as_view(), name='registration'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dasboard_view, name='dashboard'),
]

