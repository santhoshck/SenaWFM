from .models import User
from rest_framework import viewsets
from users.serializers import UserSerializer
from django.views.decorators.csrf import csrf_exempt

class UserViewSet (viewsets.ModelViewSet):  
    serializer_class = UserSerializer   
    queryset = User.objects.all()