from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.urls import reverse
import time
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def register(request):
    # if request.user.is_authenticated:
    #     return redirect(reverse('home'))
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            messages.success(request, 'Your account has been created! You are now able to log in')
            new_user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password1'],
                                )
            login(request, new_user)
            return redirect('index')
 

    else:
        form = UserRegisterForm()
    return render(request, 'users/signup.html', {'form': form})


@login_required
def logout_user(request):

    logout(request)
    messages.success(request, 'You are logged out successfully')
    return redirect('login')