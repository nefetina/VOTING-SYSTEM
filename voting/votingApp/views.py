from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'activities/index.html')

def newreg(request):
    return render(request, 'activities/newreg.html')

def homepage(request):
    return render(request, 'activities/homepage.html')

def result(request):
    return render(request, 'activities/result.html')

def comelec(request):
    return render(request, 'activities/comelec.html')

def application(request):
    return render(request, 'activities/application.html')