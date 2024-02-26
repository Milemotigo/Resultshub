from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'generics/index.html')

def login(request):
    return render(request, 'generics/login.html')

def signup(request):
    return render(request, 'generics/signup.html')