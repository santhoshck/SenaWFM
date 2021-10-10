from rest_framework import serializers
from .models import OrgUnit, Employee

class OrgUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgUnit
        fields = ('id','ou_id' ,'ou_name', 'manager', 'delegate', 'parent_ou', 'comments', 'is_active')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id','employee_id', 'full_name', 'category', 'job_grade', 
            'entry_date', 'exit_date', 'email', 'supervisor', 'org', 'org_unit', 
            'time_percent', 'sex', 'comments', 'is_active', 'is_org_admin', 'history', 'user')