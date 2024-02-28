from django.urls import path
from student.views import UserFormView, login

app_name = 'student'

urlpatterns = [
    path('registration/', UserFormView.as_view(), name='registration'),
    path('login/', login, name='login'),
]

