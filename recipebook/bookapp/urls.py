from django.contrib import admin
from django.urls import path
from . import views

app_name="bookapp"

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.signup, name="signup")
]
