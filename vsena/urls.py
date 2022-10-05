from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

#from django.views.generic import TemplateView
from django.urls import path, include
from organization.urls import router as OrganizationRouter
from users.urls import router as UserRouter
from pages import views

router = routers.DefaultRouter()
router.registry.extend(OrganizationRouter.registry)
router.registry.extend(UserRouter.registry)

urlpatterns = [
    #path('', views.home_view, name='home'),
    path('admin/', admin.site.urls),
    #path('accounts/', include('allauth.urls')),
    #path('about/',TemplateView.as_view(template_name='pages/about.html'),name='about'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]