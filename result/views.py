from django.shortcuts import render

def result(request):
    return render(request, 'generics/index.html')               

