from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import registration

class StudentRegistration(UserCreationForm):
    class Meta:
        model = registration
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name', 'idno', 'userType']
