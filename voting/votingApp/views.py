from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentRegistration
from .models import candidates, vote, registration
from django.core.mail import send_mail
from django.conf import settings
import mysql.connector as sql


installed_apps = ['votingApp']

# Create your views here.
def index(request):#login student
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.userType == 'STDNT':
            login(request, user)
            return redirect('/homepage')

        elif user is not None and user.userType == 'COMSELEC':
            login(request, user)
            return redirect('/comelec')
        
        else:
            messages.info(request, 'INVALID CREDENTIALS')

    return render (request, 'votingApp/index.html')

def newreg1(request):# student registration
    form = StudentRegistration()
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/index')
    context =  {'form': form }
    return render(request, 'votingApp/newreg.html', context)

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
        
        datas = candidates.objects.create(firstname=firstname, surname=surname, course=course, age=age, gender=gender, position=position, partylist=partylist, image=image, description=lala)
        datas.save()
    
        return redirect('/homepage')
    
def delete(request, id):
    data = candidates.objects.get(id=id)
    data.delete()
    return redirect('/comelec')

@login_required(login_url='/index')
def homepage(request):
    if request.user.is_authenticated and request.user.userType == 'STDNT':
        data = registration.objects.filter(idno = request.user.pk)
        context = { 'data': data}
        return render(request, 'votingApp/homepage.html', context)
    return redirect('/index')

#@login_required(login_url='/index')
def result(request):
    if request.user.is_authenticated and request.user.userType == 'STDNT':
        return render(request, 'votingApp/result.html')
    return render(request, 'votingApp/result.html')


def comelec(request):
    #if request.user.is_authenticated and request.user.userType == 'COMSELEC':
        data = candidates.objects.all()
        return render(request, 'votingApp/comelec.html', {'data':data})
    #return redirect('/index')

@login_required(login_url='/index')
def application(request):
    if request.user.is_authenticated and request.user.userType == 'STDNT':
        return render(request, 'votingApp/application.html')
    return redirect('/index')

@login_required(login_url='/index')
def voting(request):
    if request.user.is_authenticated and request.user.userType == 'STDNT':
        data = registration.objects.filter(idno = request.user.pk)
        print(data)
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
            'data': data
        }
        return render(request, 'votingApp/voting.html', context)
    return redirect ('/index')


def votinga(request):
    if request.method == 'POST':
        idno_id = request.POST.get('idno_id')
        president = request.POST.get('president')
        vicepresident = request.POST.get('vice')
        secretary = request.POST.get('secretary')
        asec = request.POST.get('asec')
        treasurer = request.POST.get('treasurer')
        auditor = request.POST.get('auditor')
        senator1 = request.POST.get('senator1')
        senator2 = request.POST.get('senator2')
        senator3 = request.POST.get('senator3')
        senator4 = request.POST.get('senator4')
        senator5 = request.POST.get('senator5')
        senator6 = request.POST.get('senator6')
        governor = request.POST.get('governor')
        governor1 = request.POST.get('governor1')
        governor2 = request.POST.get('governor2')
        governor3 = request.POST.get('governor3')
        governor4 = request.POST.get('governor4')
        governor5 = request.POST.get('governor5')
        governor6 = request.POST.get('governor6')
        governor7 = request.POST.get('governor7')
        governor8 = request.POST.get('governor8')
        governor9 = request.POST.get('governor9')

        votes = vote.objects.create(idno_id=idno_id, president=president, vicepresident=vicepresident,secretary=secretary, asec=asec, treasurer=treasurer, auditor=auditor, senator1=senator1, senator2=senator2, senator3=senator3, senator4=senator4, senator5=senator5, senator6=senator6, governor=governor, governor1=governor1, governor2=governor2, governor3=governor3, governor4=governor4, governor5=governor5, governor6=governor6, governor7=governor7, governor8=governor8, governor9=governor9)
        votes.save()

        ids = registration.objects.get(idno = request.user.pk)
        ids.status = 'VOTED'
        ids.save()
        return redirect ('/homepage')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            name, #name of sender
            email + "\n" + message, #subject
            email,
            ['codemtv1429@gmail.com'],
        )
        
        return redirect('/index')
    else:
        return render(request, 'votingApp/contact.html')

def comresult(request):
    return render(request, 'votingApp/comresult.html')
    
def pdf(request):
    #if request.user.is_authenticated and request.user.userType == 'COMSELEC':
        data = candidates.objects.all()
        return render(request, 'votingApp/pdf.html', {'data':data})
    #return redirect('/index')
    
def logoutUser(request):
    logout(request)
    return redirect('/index')

