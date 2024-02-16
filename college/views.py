from django.shortcuts import render

def school_view(request):
    return render(request, 'generics/index.html')

