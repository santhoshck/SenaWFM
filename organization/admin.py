from django.contrib import admin

# Register your models here.
from .models import Person,OrgUnit

@admin.register (Person)
class PersonAdmin (admin.ModelAdmin):
    list_display = ['full_name','supervisor','org_unit' ]

@admin.register (OrgUnit)
class OrgUnitAdmin (admin.ModelAdmin):
    pass