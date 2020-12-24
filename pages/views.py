from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from organization.models import OrgUnit,Employee

@login_required
def home_view (request):
    ou_changes= OrgUnit.history.all()
    emp_changes= Employee.history.all()
    context = {
        'ou_changes': ou_changes,
        'emp_changes': emp_changes
        }
    return render(request, 'pages/home.html', context)