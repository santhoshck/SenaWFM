from django.urls import path

from . import views

app_name = 'org'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('employee/<int:pk>/',views.EmployeeDetailView.as_view(),name='employee_detail'),
    #path('ou/<int:pk>/',views.OUDetailView.as_view(),name='ou_detail'),
    path ('ou/<int:ou_id>/', views.ou_detail, name = 'ou_detail'),
    path('ou_edit/<int:ou_id>', views.ou_edit, name='ou_edit'),
    path('ou_create/', views.ou_create, name='ou_create'),
]