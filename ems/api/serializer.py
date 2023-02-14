from rest_framework import serializers
from django.contrib.auth.models import User
from ems.models import Employee, Emp_Leave_appilcation

class EmpModelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password')
    class Meta:
        model = Employee
        fields = ['username', 'password', 'Ename', 'Email','Contact','Emgcontact','Address','Position','Dob','MaritalStatus','Bloodgrp','Jobtitle','Workloc','Date_of_Join','Report_to','Linkedin','Profile_pic']
      
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        employee = Employee.objects.create(user=user, **validated_data)
        return employee

   

class UpdateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
       
        fields = [ 'Ename', 'Email','Contact','Emgcontact','Address','Position','Dob','MaritalStatus','Bloodgrp','Jobtitle','Workloc','Date_of_Join','Report_to','Linkedin','Profile_pic']



class EmpnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('Ename')


class EmpLeaveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_Leave_appilcation
        fields = '__all__'


    
    
   