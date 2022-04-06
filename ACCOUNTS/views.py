from django.shortcuts import render

# Create your views here.
from ACCOUNTS.serializers import SignupSerializer
from ACCOUNTS.models import CustomUser
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class =SignupSerializer
    permission_classes = [permissions.IsAdminUser]

class SignupUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class =SignupSerializer
    

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [permissions.AllowAny] # signup all users with limited permissions allow only
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser | permissions.DjangoModelPermissions] # admin only .
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [permissions.IsAdminUser | permissions.DjangoModelPermissions ]  # admin only
        elif self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser | permissions.DjangoModelPermissions ]  # admin only
        return [permission() for permission in permission_classes]





