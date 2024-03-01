from django.urls import path    
from result.views import result

app_name = 'result'

urlpatterns = [
    path('results/', result, name='results'),
]
