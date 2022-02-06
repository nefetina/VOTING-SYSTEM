from django.shortcuts import redirect, render
#from .forms import newregForm
#import mysql.connector as sql
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import newreg
from .models import candidates
import mysql.connector as sql

installed_apps = ['votingApp']

# Create your views here.
def index(request):
    return render(request, 'votingApp/index.html')

def newreg1(request):
    return render(request, 'votingApp/newreg.html')


# user registration
def new(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        idno = request.POST.get('idno')
        password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password'),
        data = newreg.objects.create(firstname=name, email=email, idno=idno, password=password)
        data.save()
        return render(request, 'votingApp/index.html')
    
    
#     user login


# def login(request):
#     if request.method=='POST':
#         username = request.POST.get('email')
#         password = request.POST.get('pass')
#         user = authenticate(username=username, password=password)
    


def userlogin(request):
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database='vsdb')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                email=value
            if key=="pass":
                password=value
        
        c="select * from votingapp_newreg where email='{}' and password='{}'".format(email,password)
        
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'votingApp/index.html')
            
        else:
            data = newreg.objects.filter(email=email)
          
            return render(request, 'votingApp/homepage.html', {'data':data})

    return render(request, 'votingApp/index.html')
 
            

    
#                  candidates


def peoples(request):
    if request.method=='POST':
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        course = request.POST.get('course')
        age = request.POST.get('age')
        gender=request.POST.get('gender')
        position=request.POST.get('position')
        partylist=request.POST.get('partylist')
        image=request.POST.get('image')
        lala=request.POST.get('lala')
        
        datas = candidates.objects.create(firstname=firstname, surname=surname, course=course, age=age, gender=gender, position=position, partylist=partylist, image=image, description=lala)
        datas.save()
    
        return render(request, 'votingApp/homepage.html')
    
    
def delete(request, id):
    data = candidates.objects.get(id=id)
    data.delete()
    return redirect('/comelec')



def homepage(request):
    data = newreg.objects.all()
    return render(request, 'votingApp/homepage.html', {'data':data})

def result(request):
    return render(request, 'votingApp/result.html')

def comelec(request):
    nef1 = candidates.objects.all()
    return render(request, 'votingApp/comelec.html', {'nef1':nef1})

def application(request):
    return render(request, 'votingApp/application.html')

#function for newreg

#def reguser(request):
##   if form.is_valid():
 #       form.save()
  
 #   context= {'form': form }
        
 #   return render(request, 'votingApp/index.html', context)



