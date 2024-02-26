from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import collegeSerializer
from .backends import collegeAuthBackend


@login_required(login_url='login')
def school_view(request):
    return render(request, 'generics/index.html')


@api_view(['POST'])
def college_login_view(request):
    """"""
    serializer = collegeSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    college = collegeAuthBackend.authenticate(request, **serializer.validated_data)
    if college:
        login(request, college)
        return redirect('school')
    return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def college_signup_view(request):
    """"""
    serializer = collegeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Account Sucessfully Created, Please login to continue"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

