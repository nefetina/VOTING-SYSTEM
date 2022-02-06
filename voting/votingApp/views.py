from django.shortcuts import render
#from .forms import newregForm
#import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import newreg

# Create your views here.
def index(request):
    return render(request, 'votingApp/index.html')

def newreg1(request):
    return render(request, 'votingApp/newreg.html')

def new(request):
    Newreg = newreg.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
        idno = request.POST['idno'],
        password = request.POST['password'],
        confirm_password = request.POST['confirm_password'],
        )
    context = { 'Newreg' : Newreg,}
    return render(request, 'votingApp/index.html', context)

def homepage(request):
    return render(request, 'votingApp/homepage.html')

def result(request):
    return render(request, 'votingApp/result.html')

def comelec(request):
    return render(request, 'votingApp/comelec.html')

def application(request):
    return render(request, 'votingApp/application.html')

#function for newreg

#def reguser(request):
##   if form.is_valid():
 #       form.save()
  
 #   context= {'form': form }
        
 #   return render(request, 'votingApp/index.html', context)



