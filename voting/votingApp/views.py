from multiprocessing import context
from tokenize import Comment
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import StudentRegistration
from .models import candidates
from .models import vote
import mysql.connector as sql


installed_apps = ['votingApp']

# Create your views here.
def index(request):#login student
    return render(request, 'votingApp/index.html')

def newreg1(request):# student registration
    form = StudentRegistration()
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/index')
    context =  {'form': form }
    return render(request, 'votingApp/newreg.html', context)


def comeleclog(request):# comelec login
    return render(request, 'votingApp/comelec_login.html')

def regcomelec(request):# comelec signup
    return render(request, 'votingApp/comelec_reg.html')


# -------comelec registration
def regcom(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        idno = request.POST.get('idno')
        pas = request.POST.get('pas')
        # cpassword = request.POST.get('cpassword'),
        data = newreg.objects.create(name=name, email=email, idno=idno, password=pas)
        data.save()
        return render(request, 'votingApp/comelec_login.html')


# ------comelec log in
def comlog(request):
    if request.method=="POST":
        n=sql.connect(host="localhost",user="root",password="",database='voting')
        cursor=n.cursor()
        e=request.POST
        for key,value in e.items():
            if key=="email":
                email=value
            if key=="pass":
                password=value
        
        l="select * from votingapp_comelecreg where email='{}' and password='{}'".format(email,password)
        
        cursor.execute(l)
        h=tuple(cursor.fetchall())
        if h==():
            return render(request, 'votingApp/comelec_login.html')
            
        else:
            data = newreg.objects.filter(email=email)
          
            return redirect('/comelec', {'data':data})

    return render(request, 'votingApp/comeleclog.html')


def userlogin(request):
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",password="",database='voting')
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
        position=request.POST.get('pos')
        partylist=request.POST.get('partylist')
        image=request.POST.get('image')
        lala=request.POST.get('lala')
        
        datas = candidates.objects.create(name=firstname, surname=surname, course=course, age=age, gender=gender, position=position, partylist=partylist, image=image, description=lala)
        datas.save()
    
        return redirect('/homepage')
    

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

def voting(request):
    option = candidates.objects.filter(position='President')
    option1 = candidates.objects.filter(position='Vicepresident')
    option2 = candidates.objects.filter(position='Secretary')
    option3 = candidates.objects.filter(position='Asec')
    option4 = candidates.objects.filter(position='Auditor')
    option5 = candidates.objects.filter(position='Treasurer')
    option6 = candidates.objects.filter(position='Senator')
    option7 = candidates.objects.filter(position='Governor')
    context = {
        'option':option,
        'option1':option1,
        'option2':option2,
        'option3':option3,
        'option4':option4,
        'option5':option5,
        'option6':option6,
        'option7':option7,
    }
    return render(request, 'votingApp/voting.html', context)

def vote(request):
    if request.method == 'POST':
        president = request.POST.get('president')
        vicepresident = request.POST.get('vice')
        secretary = request.POST.get('secretary')
        asec = request.POST.get('asec')
        treasurer = request.POST.get('treasurer')
        auditor = request.POST.get('auditor')
        

        voted = vote.objects.create(president=president, vicepresident=vicepresident, secretary=secretary, asec=asec, treasurer=treasurer, auditor=auditor)
        voted.save()

        return redirect ('homepage/')



