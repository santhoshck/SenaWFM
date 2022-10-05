#from django.urls import path
from rest_framework import routers

from . import views

app_name = 'org'

router = routers.DefaultRouter()
router.register(r'ou',views.OrgUnitViewSet, 'ou')
router.register(r'organization', views.OrganizationViewSet, 'organization')
router.register(r'employee',views.EmployeeViewSet, 'employee')