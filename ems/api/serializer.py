from rest_framework import serializers

from ems.models import Employee

class EmpModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'