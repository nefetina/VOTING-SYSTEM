from asyncio.windows_events import NULL
from email.mime import image
from string import digits
from unicodedata import digit
from django.db import models
from django.forms import TextInput

# Create your models here.

class newreg(models.Model):
    firstname = models.CharField(max_length=15 )
    idno = models.CharField(max_length=15 )
    email = models.EmailField(max_length=50 )
    password = models.CharField(max_length=15 )
    confirm_passsword = models.CharField(max_length=1)



class application(models.Model):
    gender = [
        ('FEMALE', 'FEMALE'),
        ('MALE', 'MALE'),
    ]

    firstname = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    course = models.CharField(max_length=15)
    age = models.IntegerField()
    gender = models.CharField(max_length=7, choices=gender,)
    position = models.CharField(max_length=15)
    partylist = models.CharField(max_length=15)
    image = models.ImageField()
    description = models.CharField(max_length=600)


