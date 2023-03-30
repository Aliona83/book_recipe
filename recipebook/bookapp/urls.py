from django.urls import path
from . import views

app_name = "bookapp"

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe_list', views.all_recipes, name="recipelist"),
]
