from django.test import TestCase

from organization.models import Employee, OrgUnit, Organization, OrgDesign
from users.models import User

class EmployeeModelTests (TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(org_name="Org Name")
        OrgUnit.objects.create(ou_name="OU Name")
        OrgDesign.objects.create(field='EC', value='Permanent')

    def test_org_design (self):
        org1=Organization.objects.get(org_name="Org Name")
        ou1=OrgUnit.objects.get(ou_name="OU Name")
        emp1=Employee.objects.create(full_name="Employee Name",org=org1,org_unit=ou1)
        od=OrgDesign.objects.get(value="Permanent")
        emp1.category=od 
        self.assertEqual(emp1.category.value,'Permanent')

    def test_auto_create_user (self):
        org1=Organization.objects.get(org_name="Org Name")
        ou1=OrgUnit.objects.get(ou_name="OU Name")
        emp1=Employee.objects.create(full_name="Employee Name",org=org1,org_unit=ou1, email='employee@orgname.com')
        user1=User.objects.get(email='employee@orgname.com')
        self.assertEqual(user1.name, 'Employee Name')

class OrgUnitModelTests (TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(org_name="Org Name")
        

    def test_org_design (self):
        org1=Organization.objects.get(org_name="Org Name")
        emp1=Employee.objects.create(full_name="Employee Name1",employee_id='E-1',org=org1, email='employee1@orgname.com')
        emp2=Employee.objects.create(full_name="Employee Name2",employee_id='E-2',org=org1, email='employee2@orgname.com')
        emp3=Employee.objects.create(full_name="Employee Name3",employee_id='E-3',org=org1, email='employee3@orgname.com')
        #emp4=Employee.objects.create(full_name="Employee Name4",employee_id='E-4',org=org1, email='employee4@orgname.com')
        ou1=OrgUnit.objects.create(ou_id='OU-1',ou_name="OU Name1",manager=emp1,delegate=emp2)
        ou2=OrgUnit.objects.create(ou_id='OU-2',ou_name="OU Name2", parent_ou = ou1,manager=emp3)
        ou3=OrgUnit.objects.create(ou_id='OU-3',ou_name="OU Name3", parent_ou = ou2)
        user1=emp1.user
        user2=emp2.user
        user3=emp3.user
        self.assertTrue(ou1.is_ou_manager(user1))
        self.assertTrue(ou3.is_ou_manager(user1))
        self.assertTrue(ou2.is_ou_manager(user2))
        self.assertTrue(ou2.is_ou_manager(user3))
        self.assertFalse(ou1.is_ou_manager(user3))
        

