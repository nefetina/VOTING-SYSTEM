from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import newreg


class newregForm(forms.ModelForm):
    class Meta:
        model= newreg
        fields= ["firstname","idno", "email", "password", "confirm_passsword"]	

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']