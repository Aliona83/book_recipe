from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def index(request):
    
    return render(request, "bookapp/base.html")


def signup(request):
    form = UserCreationForm()
    return render(request, "registration/signup.html")


def home(request):
    return render(request, "bookapp/index.html")