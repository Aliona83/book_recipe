from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm


def register_user(request):
    if request.method == 'GET':
        form = RegisterForm()
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created.You can log in now') 
            return redirect(('login'))
        else:
            form = UserCreationForm()    
        context = {'form': form}   
        return render(request, 'authenticate/register_user.html') 


def login_user(request):
    return render(request, 'authenticate/login.html')


def logout_user(request):
    return render(request, 'home.html')