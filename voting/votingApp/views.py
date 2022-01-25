from django.shortcuts import render
from django.urls import path
#from django.http import HttpResponse

def index(request):
    return render(request, 'activities/index.html')

def newreg(request):
    return render(request, 'activities/newreg.html')