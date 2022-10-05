from organization.models import Organization
from rest_framework import viewsets, permissions
from organization.serializers import OrganizationSerializer

class OrganizationViewSet (viewsets.ModelViewSet):  
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    serializer_class = OrganizationSerializer   
    queryset = Organization.objects.all()