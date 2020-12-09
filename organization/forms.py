from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import OrgUnit

class OUForm (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-ouForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = OrgUnit
        #fields = ['ou_id', 'ou_name', 'manager', 'parent_ou', 'comments', 'is_active']
        fields = '__all__'
