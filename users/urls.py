from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register ,name= 'register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=LoginForm,redirect_authenticated_user=True) ,name= 'login'),
    path('logout/', views.logout_user, name='logout')
]
