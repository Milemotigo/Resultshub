from django.urls import path, include
from generics import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]