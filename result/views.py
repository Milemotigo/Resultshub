from django.shortcuts import render
from generics.models import CustomUser
from django.contrib.auth.decorators import login_required

@login_required
def result(request):
    user = CustomUser.objects.all()
    return render(request, 'generics/student/index.html' , {user: 'user'})


@login_required
def payment(request):
    return render(request, 'generics/result/payment.html')
