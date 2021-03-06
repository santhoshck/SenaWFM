from django.contrib import admin

# Register your models here.
from .models import Employee,OrgUnit, Organization, OrgDesign

@admin.register (Employee)
class EmployeeAdmin (admin.ModelAdmin):
    list_display = ['full_name','supervisor','org_unit' ]

@admin.register (OrgUnit)
class OrgUnitAdmin (admin.ModelAdmin):
    pass

@admin.register (OrgDesign)
class OrgDesignAdmin (admin.ModelAdmin):
    list_display=['field','value']

@admin.register (Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display =['org_id', 'org_name']