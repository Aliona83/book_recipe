from django.shortcuts import render
from datetime import datetime


def home(request):
    name = "Aliona"
    # get current time
    now = datetime.now()
    current_year = now.year

    # get current time
    time = now.strftime('%H:%M %p')

    return render(request, 'bookapp/home.html', {"name": name,
 "current_year": current_year, "time": time,
    })


def all_recipes(request):

    return render(request, 'bookapp/recipe_list.html', {})
