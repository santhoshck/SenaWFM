from organization.models import Organization
from rest_framework import viewsets
from organization.serializers import OrganizationSerializer

class OrganizationViewSet (viewsets.ModelViewSet):  
    serializer_class = OrganizationSerializer   
    queryset = Organization.objects.all()