from django.urls import path    
from result.views import result, payment

app_name = 'result'

urlpatterns = [
    path('results/', result, name='results'),
    path('buy-card/', payment, name='buy-card')
]
