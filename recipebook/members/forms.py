from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=65)
    email = forms.CharField(max_length=65)
    password1 = forms.CharField(max_length=65)
    password2 = forms.CharField(max_length=65)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
 

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65)