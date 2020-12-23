from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from organization.models import Employee
from organization.forms import EmployeeForm

from .view_support import *

#TODO
#PermissionDeniedView - Check the views documentation


@login_required
def employee_create (request):
    if request.method == 'POST':
        form = EmployeeForm (request.POST)    
        if form.is_valid():
            employee = form.save()
            return HttpResponseRedirect('/org/employee/'+str(employee.id))
    else:
        form = EmployeeForm()
        form.helper.form_action = '/org/employee_create/'
    return render (request, 'organization/employee_create.html', {'form':form}) 


@login_required
def employee_detail (request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    changes = historical_changes(employee.history)
    return render (request, 'organization/employee_detail.html', {'employee':employee, 'changes':changes})


@login_required
def employee_edit (request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    print ('Emp Id: '+str(emp_id))
    if request.method == 'POST':
        form = EmployeeForm (request.POST, instance=employee)    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/org/employee/'+str(emp_id))
    else:
        form = EmployeeForm(instance=employee)
        form.helper.form_action = '/org/employee_edit/'+str(employee.id)
    return render (request, 'organization/employee_edit.html', {'form':form, 'employee':employee})


class EmployeeListView(LoginRequiredMixin, generic.ListView):
    template_name = 'organization/employee_list.html'
    model = Employee
    context_object_name ='employee_list' #This is the object_list seen by template