from django.shortcuts import render
from .forms import newregForm
#import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def index(request):
    return render(request, 'votingApp/index.html')

def newreg(request):
    return render(request, 'votingApp/newreg.html')

def homepage(request):
    return render(request, 'votingApp/homepage.html')

def result(request):
    return render(request, 'votingApp/result.html')

def comelec(request):
    return render(request, 'votingApp/comelec.html')

def application(request):
    return render(request, 'votingApp/application.html')

#function for newreg

def reguser(request):
    form= newregForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'votingApp/index.html', context)

