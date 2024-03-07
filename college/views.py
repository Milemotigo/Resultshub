from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .serializers import collegeSerializer
from .backends import collegeAuthBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@login_required(login_url='login')
def school_view(request):
    return render(request, 'generics/index.html')


# @api_view(['POST'])
# @authentication_classes([SessionAuthentication])
# def college_login_view(request):
    """"""
    # serializer = collegeSerializer(data=request.data)
    # serializer.is_valid(raise_exception=True)
    # college = collegeAuthBackend.authenticate(request, **serializer.validated_data)
    # if college:
    #     login(request, college)
    #     return redirect('school')
    # return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
def college_login_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return Response({"details": "User is already authenticated"}, status=status.HTTP_200_OK)

        username = request.data.get('userDetail')
        password = request.data.get('password')
        user = collegeAuthBackend().authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"details": "Login Successful"}, status=status.HTTP_200_OK)
        return Response({"details": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"details": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)



@api_view(['POST'])
# @authentication_classes([SessionAuthentication])
# @authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
def college_signup_view(request):
    """"""
    serializer = collegeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Account Sucessfully Created, Please login to continue"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @login_required(login_url='login')
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def college_dashboard(request):
    # return Response({"details": "Welcome to College Dashboard"}, status=status.HTTP_200_OK)
    return render(request, 'college/dashboard.html')


@login_required(login_url='login')
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
def college_logout(request):
    logout(request)
    return Response({"details": "Logout Successful"}, status=status.HTTP_200_OK)

