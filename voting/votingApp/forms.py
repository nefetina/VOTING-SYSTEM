from django import forms
from .models import newreg

class newregForm(forms.ModelForm):
    class Meta:
        model= newreg
        fields= ["firstname","idno", "email", "password", "confirm_passsword"]	
