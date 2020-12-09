from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Person, OrgUnit
from .forms import OUForm

#TODO
#PermissionDeniedView - Check the views documentation

def historical_changes(history):
    changes = []
    if history is not None :
        last = history.first()
        for all_changes in range(history.count()):
            new_record, old_record = last, last.prev_record
            if old_record is not None:
                delta = new_record.diff_against(old_record)
                changes.append(delta)
            last = old_record
    return changes

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'organization/home.html'
    model = OrgUnit
    context_object_name ='ou_list' #This is the object_list seen by template

class PersonDetailView(LoginRequiredMixin, generic.DetailView):
    model = Person
    template_name = 'organization/person_detail.html'
    context_object_name = 'person'

class OUDetailView(LoginRequiredMixin, generic.DetailView):
    model = OrgUnit
    template_name = 'organization/ou_detail.html' 
    context_object_name ='ou'

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
    return render (request, 'organization/ou_edit.html', {'form':form, 'ou':ou}) 

@login_required
def ou_create (request):
    if request.method == 'POST':
        form = OUForm (request.POST)    
        if form.is_valid():
            ou = form.save()
            return HttpResponseRedirect('/org/ou/'+str(ou.id))
    else:
        form = OUForm()
    return render (request, 'organization/ou_create.html', {'form':form}) 