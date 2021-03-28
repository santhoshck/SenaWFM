from django.test import TestCase
from django.urls import reverse

from organization.models import Employee, OrgUnit, Organization
from django.contrib.auth import get_user_model


class OUViewTests (TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(org_name="Org Name")
        OrgUnit.objects.create(ou_name="OU Name")

    def test_ou_edit_permissions_is_org_admin(self):
        org1=Organization.objects.get(org_name="Org Name")
        ou1=OrgUnit.objects.get(ou_name="OU Name")
        emp1=Employee.objects.create(employee_id='EM-1',full_name="Employee Name",org=org1,org_unit=ou1,email='emp1@orgname.com',is_org_admin=True)
        login = self.client.login(username='emp1@orgname.com', password='P@ssw0rd')
        self.assertTrue(login)
        response=self.client.get(reverse('org:ou_edit',args=[str(ou1.id)]))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(str(response.context['user']), 'emp1@orgname.com')        
        self.client.logout()

    def test_ou_edit_permissions_is_staff(self):
        org1=Organization.objects.get(org_name="Org Name")
        ou1=OrgUnit.objects.get(ou_name="OU Name")
        emp1=Employee.objects.create(employee_id='EM-1',full_name="Employee Name",org=org1,org_unit=ou1,email='emp1@orgname.com')
        user1=get_user_model().objects.get(email='emp1@orgname.com')
        user1.is_staff=True
        user1.save()
        login = self.client.login(username='emp1@orgname.com', password='P@ssw0rd')
        self.assertTrue(login)
        response=self.client.get(reverse('org:ou_edit',args=[str(ou1.id)]))
        self.assertEqual(response.status_code, 200) 
        self.assertEqual(str(response.context['user']), 'emp1@orgname.com')        
        self.client.logout()

    def test_ou_edit_permissions_no_permission(self):
        org1=Organization.objects.get(org_name="Org Name")
        ou1=OrgUnit.objects.get(ou_name="OU Name")
        emp1=Employee.objects.create(employee_id='EM-1',full_name="Employee Name",org=org1,org_unit=ou1,email='emp1@orgname.com')
        login = self.client.login(username='emp1@orgname.com', password='P@ssw0rd')
        self.assertTrue(login)
        response=self.client.get(reverse('org:ou_edit',args=[str(ou1.id)]))
        self.assertEqual(response.status_code, 302)       
        self.client.logout()
