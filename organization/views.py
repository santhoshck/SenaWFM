from django.shortcuts import render, get_object_or_404

from .models import Person, OrgUnit

#TODO
#PermissionDeniedView - Check the views documentation

def index(request):
    people = Person.objects.all()
    return render (request, 'home.html', {
        'people' : people,
    })

def person_detail(request, p_id):
    person = get_object_or_404(Person, pk=p_id)
    return render (request, 'person_detail.html', {
        'person': person,
    })

def ou_detail(request, ou_id):
    ou = get_object_or_404(OrgUnit, pk=ou_id)
    return render (request, 'ou_detail.html', {
        'ou':ou,
    })

def ou_edit(request, ou_id):
    ou = get_object_or_404(OrgUnit, pk=ou_id)
    return render (request, 'ou_edit.html', {
        'ou':ou,
    })
