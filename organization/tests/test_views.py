from django.http import response
from django.urls import path, reverse, include
import pytest
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

from organization.models import Employee, OrgUnit, Organization
from ..serializers import OrgUnitSerializer

class OUViewTests (APITestCase):
        
    fixtures = ["organization/tests/Organization.json","organization/tests/OrgUnit.json",] 

    def test_login_logout(self):
        org1=Organization.objects.get(org_name="Org Name")
        ou1=OrgUnit.objects.get(ou_name="OU Name")
        emp1=Employee.objects.create(employee_id='EM-1',full_name="Employee Name",org=org1,org_unit=ou1,email='emp1@orgname.com',is_org_admin=True)
        success = self.client.login (username='emp1@orgname.com', password='P@ssw0rd')
        print(self.client.session.values())
        self.assertTrue (success)
        #self.assertEqual(1,2)
        self.client.logout()

    def test_ou_list(self):
        url = reverse('ou-list')
        response = self.client.get(url,format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.json()[0]['ou_name'],'OU Name')
        ous = OrgUnit.objects.all()
        serializer = OrgUnitSerializer(ous, many=True)
        self.assertEqual(response.data, serializer.data)

