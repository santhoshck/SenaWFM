from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model
#import rules
from rules.contrib.models import RulesModel

class Organization (RulesModel):
    #class Meta:
    #    rules_permissions = {
    #        "add": rules.is_staff,
    #        "read": rules.is_authenticated,
    #        "change": rules.is_staff,
    #    }
    org_id = models.CharField(max_length=10, unique=True )
    org_name = models.CharField (max_length=50)
    #history = HistoricalRecords()
    comments = models.TextField (null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def __str__ (self):
        return self.org_id+ ":" +self.org_name  


class Employee (RulesModel):
    #class Meta:
    #    rules_permissions = {
    #        "read": rules.is_authenticated,
    #    }
    class Sex (models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')

    employee_id = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=50)
    category = models.ForeignKey (
        'OrgDesign',
        limit_choices_to={'field':'EC'},
        related_name='emp_category',
        on_delete=models.PROTECT,
        null=True
    )
    job_grade = models.ForeignKey (
        'OrgDesign',
        limit_choices_to={'field':'JG'},
        related_name='emp_grade',
        on_delete=models.PROTECT,
        null=True
    )
    entry_date = models.DateField(help_text='Joining Date',null=True)
    exit_date = models.DateField(null=True, blank=True)
    email = models.EmailField (null = True, blank = True)
    #TODO
    #picture = models.ImageField (upload_to='uploads/%Y/%m/')
    #MEDIA_ROOT may need to be set for uploads to work
    supervisor = models.ForeignKey (
        'self',
        limit_choices_to={'is_active':True},
        related_name='team',
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    org = models.ForeignKey (
        'Organization', 
        on_delete=models.CASCADE,
        limit_choices_to={'is_active':True},
        null=True
    )
    org_unit = models.ForeignKey (
        'OrgUnit',
        limit_choices_to={'is_active':True},
        related_name='employees',
        on_delete=models.SET_NULL, 
        null = True
    )
    hours_per_week = models.IntegerField(default = 40)
    sex = models.CharField (max_length=1, choices= Sex.choices,null=True, blank= True)
    comments = models.TextField (blank=True,null=True)
    is_active = models.BooleanField(default=True)
    is_org_admin = models.BooleanField(default=False)
    history = HistoricalRecords()
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='employee',
        null=True, 
        blank=True
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.user:
            if self.email:
                user1=get_user_model().objects.create_user (self.email,'P@ssw0rd', name=self.full_name)
                self.user=user1
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__ (self):
        return self.full_name   



class OrgUnit (RulesModel):
    #class Meta:
    #    rules_permissions = {
    #        "read": rules.is_authenticated,
    #    }
    ou_id = models.CharField(max_length=20, unique=True)
    ou_name = models.CharField (max_length=50)
    manager = models.ForeignKey(
        'Employee',
        limit_choices_to={'is_active':True},
        on_delete=models.SET_NULL,
        related_name='ou_manager',
        blank=True, 
        null=True
    )
    delegate = models.ForeignKey(
        'Employee',
        limit_choices_to={'is_active':True}, 
        on_delete=models.SET_NULL, 
        related_name='ou_delegate',
        blank=True, 
        null=True
    )
    parent_ou = models.ForeignKey (
        'self', 
        limit_choices_to={'is_active':True},
        on_delete=models.SET_NULL, 
        related_name='children',
        blank=True, 
        null=True 
    )
    comments = models.TextField (blank=True,null=True)
    is_active = models.BooleanField(default=True)
    history = HistoricalRecords()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    modified = models.DateTimeField(auto_now=True, editable=False)

    def is_ou_manager(self, u):
        if not u or not u.employee:
            return False
        ou = self
        while ou:
            if u.employee == ou.manager or u.employee == ou.delegate:
                return True
            if not ou.parent_ou or ou.parent_ou == ou:
                return False
            ou = ou.parent_ou 
        return False
            
    def __str__ (self):
        return self.ou_name



class OrgDesign (models.Model):
    class Field (models.TextChoices):
        EMP_CATEGORY = 'EC', _('Employee Category')
        JOB_GRADE = 'JG', _('Job Grade')

    field = models.CharField (max_length=2, choices= Field.choices)
    value = models.CharField(max_length=50)
    remarks = models.CharField (max_length=100, null=True, blank=True)

    def __str__(self):
        return self.value

    class Meta:
        unique_together = [['field','value']]