from django.urls import path
from . import views

urlpatterns = [
    path('gethelp/', views.helpreq, name='help_request'),
  
]

