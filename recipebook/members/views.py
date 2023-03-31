from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('recipe_list')
        else: 
            return render(request, 'authenticate/login.html', {'user':user})


def logout_user(request):
    logout(request)
    messages.success(request, ("yOU SDBCJHDBJ"))
    return redirect('home')


def register_user(request):
    return render(request, 'authenticate/registration_user.html')  
