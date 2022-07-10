from enum import auto
from pickle import TRUE
from urllib.parse import MAX_CACHE_SIZE
from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
import os

# Create your models here.
def filename(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timenow, old_filename)
    return os.path.join('uploads/', filename)

class registration(AbstractUser):
    userType = [
        ('STDNT', 'Student'),
        ('COMSELEC', 'Comelec'),
    ]
    idno = models.CharField(max_length=15, verbose_name='idno', null=False, primary_key=True)
    userType = models.CharField(max_length=30, choices= userType, verbose_name='userType', default ='STDNT')
    status = models.CharField(max_length=30, verbose_name='status', default='NOT VOTED')

class candidates(models.Model):
    gender = [
        ('FEMALE', 'FEMALE'),
        ('MALE', 'MALE'),
    ]
    pos = [
        ('PRESIDENT','PRESIDENT'),
        ('VICEPRESIDENT','VICEPRESIDENT'),
        ('SECRETARY','SECRETARY'),
        ('ASEC', 'ASEC'),
        ('TREASURER','TREASURER'),
        ('AUDITOR','AUDITOR'),
        ('SENATOR','SENATOR'),
        ('GOVERNOR','GOVERNOR'),
    ]
    firstname = models.CharField(max_length=15, null=False)
    surname = models.CharField(max_length=15,null=False)
    course = models.CharField(max_length=15, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=7, choices=gender,null=False)
    position = models.CharField(max_length=15,choices=pos, null=False)
    partylist = models.CharField(max_length=15,null=False)
    image = models.ImageField(upload_to='filepath', null=False)
    description = models.CharField(max_length=600, null=False)

#elec yr,
class vote(models.Model):
    idno = models.ForeignKey(registration, on_delete=models.CASCADE, related_name='ids', verbose_name = 'idno')
    date = models.DateField(auto_now_add = True)
    president = models.CharField(max_length=30)
    vicepresident = models.CharField(max_length=30)
    secretary = models.CharField(max_length=30)
    asec = models.CharField(max_length=30)
    treasurer = models.CharField(max_length=30)
    auditor = models.CharField(max_length=30)
    senator1 = models.CharField(max_length=30)
    senator2 = models.CharField(max_length=30)
    senator3 = models.CharField(max_length=30)
    senator4 = models.CharField(max_length=30)
    senator5 = models.CharField(max_length=30)
    senator6 = models.CharField(max_length=30)
    governor = models.CharField(max_length=30)
    governor1 = models.CharField(max_length=30)
    governor2 = models.CharField(max_length=30)
    governor3 = models.CharField(max_length=30)
    governor4 = models.CharField(max_length=30)
    governor5 = models.CharField(max_length=30)
    governor6 = models.CharField(max_length=30)
    governor7 = models.CharField(max_length=30)
    governor8 = models.CharField(max_length=30)
    governor9 = models.CharField(max_length=30)

class mail(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=500)

class result(models.Model):
    name = models.CharField(max_length=50)
    vote = models.IntegerField(max_length=10)
