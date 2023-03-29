from django.shortcuts import render
from datetime import datetime

def home(request):
    name = "Aliona"
    # get current time
    now = datetime.now()
    current_year = now.year

    # get current time
    time = now.striftime('%H:%M:%S %p')

    return render(request, 'home.html', {"name": name,
    "current_year": current_year,"time": time,

    })
