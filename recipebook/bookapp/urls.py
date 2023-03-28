from django.contrib import admin
from django.urls import path
from .views import *

app_name="bookapp"

urlpatterns = [
    path('', home, name="home"),
    path('signup/', signup, name="signup")
]
