from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import newreg
from .models import candidates
from .models import comelecreg
from .models import president
from .models import vicepresident
from .models import secretary
from .models import treasurer
from .models import auditor
from .models import senator
from .models import governor
import mysql.connector as sql

installed_apps = ['votingApp']

# Create your views here.
def index(request):#login student
    return render(request, 'votingApp/index.html')

def newreg1(request):# signup student
    return render(request, 'votingApp/newreg.html')

# student registration
def new(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        idno = request.POST.get('idno')
        password = request.POST.get('password')
        # confirm_password = request.POST.get('confirm_password'),
        data = newreg.objects.create(name=name, email=email, idno=idno, password=password)
        data.save()
        return render(request, 'votingApp/index.html')



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
        data = comelecreg.objects.create(name=name, email=email, idno=idno, password=pas)
        data.save()
        return render(request, 'votingApp/comelec_login.html')


# ------comelec log in
def comlog(request):
    if request.method=="POST":
        n=sql.connect(host="localhost",user="root",password="",database='vsdb')
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
            data = comelecreg.objects.filter(email=email)
          
            return redirect('/comelec', {'data':data})

    return render(request, 'votingApp/comeleclog.html')


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
    return render(request, 'votingApp/voting.html')

def voting1(request):
    return render (request, 'votingApp/voting1.html')

def president(request):
    pres=president.objects.all
    return render(request, "votingApp/voting.html",{"president":pres})

def vicepresident(request):
    vp=vicepresident.objects.all
    return render(request, "votingApp/voting.html",{"vicepresident":vp})

def secretary(request):
    sec=secretary.objects.all
    return render(request, "votingApp/voting.html",{"secretary":sec})

def Asecretary(request):
    asec=secretary.objects.all
    return render(request, "votingApp/voting.html",{"secretary":asec})

def treasurer(request):
    trsr=treasurer.objects.all
    return render(request, "votingApp/voting.html",{"treasurer":trsr})

def auditor(request):
    audit=auditor.objects.all
    return render(request, "votingApp/voting.html",{"auditor":audit})

def senator(request):
    sen1=senator.objects.all
    return render(request, "votingApp/voting1.html",{"senator":sen1})

def senator1(request):
    sen2=senator.objects.all
    return render(request, "votingApp/voting1.html",{"senator1":sen2})

def senator2(request):
    sen3=senator.objects.all
    return render(request, "votingApp/voting1.html",{"senator2":sen3})

def senator3(request):
    sen4=senator.objects.all
    return render(request, "votingApp/voting1.html",{"senator3":sen4})

def senator4(request):
    sen5=senator.objects.all
    return render(request, "votingApp/voting1.html",{"senator4":sen5})

def governor(request):
    gov1=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor":gov1})

def governor1(request):
    gov2=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor1":gov2})

def governor2(request):
    gov3=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor2":gov3})

def governor3(request):
    gov4=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor3":gov4})

def governor4(request):
    gov5=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor4":gov5})

def governor5(request):
    gov6=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor5":gov6})

def governor6(request):
    gov7=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor6":gov7})

def governor7(request):
    gov8=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor7":gov8})

def governor8(request):
    gov9=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor8":gov9})

def governor9(request):
    gov0=governor.objects.all
    return render(request, "votingApp/voting1.html",{"governor9":gov0})