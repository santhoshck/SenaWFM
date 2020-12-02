from django.forms import ModelForm
from .models import OrgUnit

class OUForm (ModelForm):
    class Meta:
        model = OrgUnit
        #fields = ['ou_id', 'ou_name', 'manager', 'parent_ou', 'comments', 'is_active']
        fields = '__all__'
