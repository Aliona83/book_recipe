from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def index(request):
    form = UserCreationForm()
    return render(request, "bookapp/index.html")


def signup(request):
    return render(request, "registration/signup.html", {"form": form})


def home(request):
    return render(request, "bookapp/home.html")