from django.urls import path
from .views import school_view

urlpatterns = [
    path('', school_view, name='school'),
]

