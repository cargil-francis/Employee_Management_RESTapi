from django.db import models


# Create your models here.
class Employee(models.Model):
    Ename=models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Contact=models.CharField(max_length=30)
    Emgcontact=models.CharField(max_length=30)
    Address=models.TextField(max_length=500)
    Position=models.CharField(max_length=250)
    Dob = models.DateField(max_length=10)
    MariialStatus=models.BooleanField()
    Bloodgrp=models.CharField(max_length=10)
    Jobtitle=models.CharField(max_length=100)
    Workloc=models.TextField(max_length=500)
    Date_of_Join=models.DateField()
    Report_to=models.CharField(max_length=250)
    Linkedin=models.URLField()
    Profile_pic=models.ImageField()
    


