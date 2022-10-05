from rest_framework import routers

from . import views

app_name = 'users'

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet, 'users')