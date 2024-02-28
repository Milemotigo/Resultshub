from django.urls import path
from .views import StudentRegistrationView

app_name = 'student'

urlpatterns = [
        path('registration/', StudentRegistrationView.as_view(), name='student')
]
