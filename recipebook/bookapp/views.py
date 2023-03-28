from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.


def home(request):
    return render(request, "bookapp/base.html")


def signup(request):
    form = UserCreationForm()
    return render(request, "registration/signup.html")

