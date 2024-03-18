from django.shortcuts import render
from .forms import collegeSignUpForm

# Create your views here.

def index(request):
    return render(request, 'generics/index.html')

def login(request):
    return render(request, 'generics/login.html')

def signup(request):
    form = collegeSignUpForm()
    return render(request, 'generics/signup.html', {'form': form})