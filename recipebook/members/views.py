from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {request.user}.")
    if user is not None:
        login(request, user)
        return redirect('login')
    else: 
        return render(request, 'authenticate/login.html')

def logout_user(selfrequest):
    if request.method == "POST":
        auth.logout(request)
    return redirect('login')


def register_user(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {request.user}.")
        context = {'form':form}

    
        form = UserCreationForm(request.POST)
        

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login = (request, user)
            messages.success(request, ("Registration seccesfull"))
            return redirect('recipe_list')
        else:
            form = UserCreationForm() 
    return render(request, 'authenticate/register_user.html', {})  
