from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import OrgUnit
from organization.forms import OUForm

from .view_support import *

#TODO
#PermissionDeniedView - Check the views documentation

@login_required
def ou_create (request):
    if request.method == 'POST':
        form = OUForm (request.POST)    
        if form.is_valid():
            ou = form.save()
            return HttpResponseRedirect('/org/ou/'+str(ou.id))
    else:
        form = OUForm()
        form.helper.form_action = '/org/ou_create/'
    return render (request, 'organization/ou_create.html', {'form':form}) 


@login_required
def ou_detail (request, ou_id):
    ou = get_object_or_404(OrgUnit, pk=ou_id)
    changes = historical_changes(ou.history)
    return render (request, 'organization/ou_detail.html', {'ou':ou, 'changes':changes})
    

@login_required
def ou_edit (request, ou_id):
    ou = get_object_or_404(OrgUnit, pk=ou_id)
    if request.method == 'POST':
        form = OUForm (request.POST, instance=ou)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/org/ou/'+str(ou_id))
    else:
        form = OUForm(instance=ou)
        form.helper.form_action = '/org/ou_edit/'+str(ou.id)
    return render (request, 'organization/ou_edit.html', {'form':form, 'ou':ou}) 


class OUListView(LoginRequiredMixin, generic.ListView):
    template_name = 'organization/ou_list.html'
    model = OrgUnit
    context_object_name ='ou_list' #This is the object_list seen by template
