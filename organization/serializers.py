from rest_framework import serializers
from rest_framework.relations import ManyRelatedField, PrimaryKeyRelatedField
from .models import OrgUnit, Employee, Organization

class OrgUnitSerializer(serializers.ModelSerializer):
    employees = serializers.PrimaryKeyRelatedField(many=True, queryset = Employee.objects.filter (is_active=True))
    #children = serializers.PrimaryKeyRelatedField(many = True, queryset=OrgUnit.objects.all)
    class Meta:
        model = OrgUnit
        fields = ('id','ou_id' ,'ou_name', 'manager', 'delegate', 'parent_ou', 'comments', 'is_active', 'employees')
        #fields = ('id','ou_id' ,'ou_name', 'manager', 'delegate', 'parent_ou', 'children', 'comments', 'is_active', 'employees')

class EmployeeSerializer(serializers.ModelSerializer):
    #team = EmployeeSerializer(many=True, read_only = True)
    team = serializers.PrimaryKeyRelatedField (many=True, queryset = Employee.objects.filter(is_active=True))
    class Meta:
        model = Employee
        fields = ('id','employee_id', 'full_name', 'category', 'job_grade', 
            'entry_date', 'exit_date', 'email', 'supervisor', 'org', 'org_unit', 
            'hours_per_week', 'sex', 'comments', 'is_active', 'is_org_admin', 'team', 'user')

class OrganizationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('org_id', 'org_name', 'comments', 'is_active')