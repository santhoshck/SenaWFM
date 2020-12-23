from django.urls import path

from . import views

app_name = 'org'
urlpatterns = [
    path('organization/<int:pk>/',views.OrganizationDetailView.as_view(),name='org_detail'),

    path('ou/list', views.OUListView.as_view(), name='ou_list'),
    #path('ou/<int:pk>/',views.OUDetailView.as_view(),name='ou_detail'),
    path ('ou/<int:ou_id>/', views.ou_detail, name = 'ou_detail'),
    path('ou_edit/<int:ou_id>', views.ou_edit, name='ou_edit'),
    path('ou_create/', views.ou_create, name='ou_create'),

    path ('employee/list/',views.EmployeeListView.as_view(),name='employee_list'),
    path('employee/<int:emp_id>/',views.employee_detail,name='employee_detail'),
    path('employee_create/',views.employee_create, name='employee_create'),
    path('employee_edit/<int:emp_id>', views.employee_edit, name='employee_edit'),
]