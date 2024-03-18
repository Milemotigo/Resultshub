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
from generics.forms import collegeSignUpForm
from django.contrib import messages


# @login_required(login_url='login')
def college_main(request):
    return render(request, 'college/index.html')


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



# @api_view(['POST'])
# @authentication_classes([SessionAuthentication])
# @authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
def college_signup_view(request):
    """"""
    if request.method == 'POST':
        form = collegeSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = collegeSignUpForm()
    return render(request, 'generics/signup.html', {'form': form})
        

# @api_view(['POST'])
# @authentication_classes([BasicAuthentication])
def college_login_view(request):
    if request.method == 'POST':
        # if request.user.is_authenticated:
        #     return Response({"details": "User is already authenticated"}, status=status.HTTP_200_OK)

        username = request.POST['inputCredentials']
        password = request.POST['inputPassword']
        user = collegeAuthBackend().authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user, backend='college.backends.collegeAuthBackend')
            return redirect('college_dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return redirect('login')



@login_required(login_url='login')
def college_dashboard(request):
    # return Response({"details": "Welcome to College Dashboard"}, status=status.HTTP_200_OK)
    return render(request, 'college/index.html')


@login_required(login_url='login')
# @api_view(['GET'])
def college_logout(request):
    # permission_classes[IsAuthenticated]
    logout(request)
    return redirect('login')

