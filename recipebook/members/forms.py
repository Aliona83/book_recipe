from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.CharField()
    password = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'pass1', 'pass2']





