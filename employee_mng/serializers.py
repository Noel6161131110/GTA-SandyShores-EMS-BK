from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','age','date_of_joining','designation','email','phone_number','gender']
        
        

class GetEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id','name','age','date_of_joining','assigned_role','designation','email','phone_number','gender']