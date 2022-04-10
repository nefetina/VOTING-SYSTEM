from django.contrib.auth.models import AbstractUser
from pyexpat import model
from django import db
from django.db import models
from django.db import connections
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
    idno = models.CharField(max_length=15, null=False)
    userType = models.CharField(max_length=30, choices= userType, verbose_name='userType', default ='STDNT')
    

#table + status voting  

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
    name = models.CharField(max_length=15, null=False)
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
    voter = models.CharField(max_length=30)
    president = models.CharField(max_length=30)
    vicepresident = models.CharField(max_length=30)
    secretary = models.CharField(max_length=30)
    asec = models.CharField(max_length=30)
    treasurer = models.CharField(max_length=30)
    auditor = models.CharField(max_length=30)
    senator = models.CharField(max_length=30)
    governor = models.CharField(max_length=30)



