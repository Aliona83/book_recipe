from django.contrib import admin
from django.urls import path
from bookapp import views

app_name="bookapp"

urlpatterns = [
    path('', views.index, name="index"),
   
]
