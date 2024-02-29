from django.urls import path
from student.views import StudentRegistrationView, StudentLoginView, logout

app_name = 'student'

urlpatterns = [
    path('registration/', StudentRegistrationView.as_view(), name='registration'),
    path('login/', StudentLoginView.as_view(), name='login'),
    path('logout/', logout, name='logout')
]

