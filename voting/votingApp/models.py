
from django.db import models
import datetime
import os

# Create your models here.
def filename(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename = "%s%s", (timenow, old_filename)
    return os.path.join('uploads/', filename)

class newreg(models.Model):
    name = models.CharField(max_length=15, null=False)
    idno = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=15,null=False)
    
class comelecreg(models.Model):
    name = models.CharField(max_length=15, null=False)
    idno = models.CharField(max_length=15, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=15,null=False)

class candidates(models.Model):
    gender = [
        ('FEMALE', 'FEMALE'),
        ('MALE', 'MALE'),
    ]

    firstname = models.CharField(max_length=15, null=False)
    surname = models.CharField(max_length=15,null=False)
    course = models.CharField(max_length=15, null=False)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=7, choices=gender,null=False)
    position = models.CharField(max_length=15, null=False)
    partylist = models.CharField(max_length=15,null=False)
    image = models.ImageField(upload_to='filepath', null=False)
    description = models.CharField(max_length=600, null=False)


