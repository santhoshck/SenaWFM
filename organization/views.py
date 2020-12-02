from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Person, OrgUnit
from .forms import OUForm

#TODO
#PermissionDeniedView - Check the views documentation

class IndexView(generic.ListView):
    template_name = 'home.html'
    model = OrgUnit
    context_object_name ='ou_list' #This is the object_list seen by template

class PersonDetailView(generic.DetailView):
    model = Person
    template_name = 'person_detail.html'
    context_object_name = 'person'

class OUDetailView(generic.DetailView):
    model = OrgUnit
    template_name = 'ou_detail.html' 
    context_object_name ='ou'

def ou_edit (request, ou_id):
    ou = get_object_or_404(OrgUnit, pk=ou_id)
    if request.method == 'POST':
        form = OUForm (request.POST, instance=ou)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/org/')
    else:
        form = OUForm(instance=ou)
    return render (request, 'ou_edit.html', {'form':form, 'ou':ou}) 

def ou_create (request):
    if request.method == 'POST':
        form = OUForm (request.POST)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/org/')
    else:
        form = OUForm()
    return render (request, 'ou_create.html', {'form':form}) 