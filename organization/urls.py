from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('person/<int:p_id>/',views.person_detail,name='person_detail'),
    path('ou/<int:ou_id>/',views.ou_detail,name='ou_detail'),
]