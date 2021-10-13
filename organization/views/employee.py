from organization.models import Employee

#TODO
#PermissionDeniedView - Check the views documentation

from rest_framework import viewsets
from organization.serializers import EmployeeSerializer

class EmployeeViewSet (viewsets.ModelViewSet):  
    serializer_class = EmployeeSerializer   
    queryset = Employee.objects.all()