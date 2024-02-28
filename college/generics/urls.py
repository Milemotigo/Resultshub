from django.urls import path, include
from generics import views

urlpatterns = [
    path('home/', views.index, name='index'),
]