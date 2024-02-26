from django.urls import path
from .views import school_view, college_login_view, college_signup_view

urlpatterns = [
    path('school/', school_view, name='school'),
    path('college_login/', college_login_view, name='college_login'),
    path('college_signup/', college_signup_view, name='college_signup'),
]

