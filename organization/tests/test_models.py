from django.test import TestCase

from organization.models import Employee, OrgUnit, Organization, OrgDesign

class EmployeeModelTests (TestCase):
    def setUp(self):
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


    

    

