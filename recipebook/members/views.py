from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        myuser = authenticate(username=username, password=pass1)
    if request.user.is_authenticated:
        return HttpResponse(f"You are already authenticated as {request.user}.")
    if myuser is not None:
        if myuser.is_active:
            login(request, myuser)
        message.success(request, "Login success")
        return redirect('bookapp/recipe_list.html')
    else: 
        message.error(request, "Invalid Credentails")
        return render(request, 'authenticate/login.html', {'myuser': myuser}, context)
    return render(request, 'login.html')   


def register_user(request):
    myuser = RegisterForm(request.POST)
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass1")
        confirmpassword = request.POST.get("pass2")
        if password != confirmpassword:
            message.warning(request, "Password is Incorrect")
            return redirect('authenticate/register_user')

        try:
            if User.objects.get(username=username):
                message.info(request, "Username is taken")
                return redirect('authenticate/register_user')
        except:
            pass
        try:
            if User.objects.get(email=email):
                messages.info(request, "Email Is Taken")
                return redirect('authenticate/register_user')
        except:
            pass
    
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "Signup Success Please login!")
        return redirect('/login.html')
              
    return render(request, 'authenticate/register_user.html')
        

def logout_user(selfrequest):
    auth.logout(request)
    return redirect('home') 
        