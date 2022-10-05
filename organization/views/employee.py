from organization.models import Employee

#TODO
#PermissionDeniedView - Check the views documentation

from rest_framework import viewsets, permissions
from organization.serializers import EmployeeSerializer

class EmployeeViewSet (viewsets.ModelViewSet):  
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    serializer_class = EmployeeSerializer   
    queryset = Employee.objects.all()