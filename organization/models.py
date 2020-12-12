from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords

class Organization (models.Model):
    org_id = models.CharField(max_length=10, unique=True )
    org_name = models.CharField (max_length=50)
    comments = models.TextField (blank=True)
    is_active = models.BooleanField(default=True)

class Employee (models.Model):
    class Sex (models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    entry_date = models.DateField(help_text='Joining Date')
    exit_date = models.DateField()
    email = models.EmailField (null = True, blank = True)
    #picture = models.ImageField (upload_to='uploads/%Y/%m/')
    #MEDIA_ROOT may need to be set for uploads to work
    supervisor = models.ForeignKey ('self',on_delete=models.SET_NULL, null=True, blank=True)
    org = models.ForeignKey ('Organization', on_delete=models.CASCADE, null=True)
    org_unit = models.ForeignKey ('OrgUnit', on_delete=models.SET_NULL, null = True)
    time_percent = models.IntegerField('100 if Full Time')
    sex = models.CharField (max_length=1, choices= Sex.choices, blank= True)
    comments = models.TextField (blank=True,null=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True)

    def __str__ (self):
        return self.full_name   




class OrgUnit (models.Model):
    ou_id = models.CharField(max_length=20, unique=True)
    ou_name = models.CharField (max_length=50)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, blank=True, null=True)
    org = models.ForeignKey ('Organization', on_delete=models.CASCADE, null=True)
    parent_ou = models.ForeignKey ('self', on_delete=models.SET_NULL, blank=True, null=True )
    comments = models.TextField (blank=True,null=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()
            
    def __str__ (self):
        return self.ou_name
    