from django.db import models
from django.contrib.auth.models import User



# Create your models here.



class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Ename = models.CharField(max_length=250)
    Email = models.EmailField(max_length=250)
    Contact = models.CharField(max_length=30)
    Emgcontact = models.CharField(max_length=30)
    Address = models.TextField(max_length=500)
    Position = models.CharField(max_length=250)
    Dob = models.DateField(max_length=10 ,null=True)
    MariialStatus = models.BooleanField()
    Bloodgrp = models.CharField(max_length=10)
    Jobtitle = models.CharField(max_length=100)
    Workloc = models.TextField(max_length=500)
    Date_of_Join = models.DateField(null=True)
    Report_to = models.CharField(max_length=250)
    Linkedin = models.URLField()
    Profile_pic = models.ImageField()

class Emp_Leave_appilcation(models.Model):
    Empid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Apply_date = models. DateField(auto_now_add=True)
    Nature_of_leave = models.CharField(max_length=255)
    First_day = models.DateField()
    Last_day = models.DateField()
    Number_of_days = models.SmallIntegerField()
    LeaveStatus = models.IntegerField(default=2)

    
    
    


