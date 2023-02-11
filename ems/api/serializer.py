from rest_framework import serializers

from ems.models import Employee, Emp_Leave_appilcation

class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
       
        fields = '__all__'



class EmpnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('Ename')


class EmpLeaveModelSerializer(serializers.ModelSerializer):
   # employee = EmpnameSerializer()
    class Meta:
        model = Emp_Leave_appilcation
        fields = '__all__'


    
    
   