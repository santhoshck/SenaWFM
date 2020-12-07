from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from organization.models import OrgUnit

@login_required
def home_view (request):
    change_history= OrgUnit.history.all()
    context = {'change_history': change_history}
    return render(request, 'pages/home.html', context)