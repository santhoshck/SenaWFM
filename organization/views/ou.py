from django.shortcuts import render
from organization.serializers import OrgUnitSerializer 
from rest_framework import viewsets      
from organization.models import OrgUnit                 

class OrgUnitViewSet(viewsets.ModelViewSet):  
    serializer_class = OrgUnitSerializer   
    queryset = OrgUnit.objects.all()