from django.urls import path, include
from generics import views

app_name = 'generics'

urlpatterns = [
    path('home/', views.index, name='index'),
]
