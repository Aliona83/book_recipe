from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "bookapp/index.html")


def signup(request):
    return render(request, "registration/signup.html")


def home(request):
    return render(request, "bookapp/home.html")