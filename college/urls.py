from django.urls import path
from .views import college_main, college_login_view, college_signup_view, college_dashboard, college_logout

urlpatterns = [
    path('college_main/', college_main, name='college_main'),
    path('college_login/', college_login_view, name='college_login'),
    path('college_signup/', college_signup_view, name='college_signup'),
    path('college_dashboard/', college_dashboard, name='college_dashboard'),
    path('college_logout/', college_logout, name='college_logout'),
]

