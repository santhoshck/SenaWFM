from django.shortcuts import render
from django.http import Http404

from .models import Person, OrgUnit


def index(request):
    people = Person.objects.all()
    return render (request, 'home.html', {
        'people' : people,
    })

def person_detail(request, p_id):
    try:
        person = Person.objects.get(id=p_id)
    except Person.DoesNotExist:
        raise Http404('Person Not found')
    return render (request, 'person_detail.html', {
        'person': person,
    })

def ou_detail(request, ou_id):
    try:
        ou = OrgUnit.objects.get(id=ou_id)
    except OrgUnit.DoesNotExist:
        raise Http404('Organization Unit Not found')
    return render (request, 'ou_detail.html', {
        'ou':ou,
    })