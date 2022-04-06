from django.contrib.auth.models import Permission
from django.shortcuts import render
from ACCOUNTS.permissions import IsAdmin, IsStudent
from BOOKS.models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from BOOKS.serializers import BookSerializer

# Create your views here.
"""
  
● Add a Book 
● Update an entry of a book 
● Delete a book 
● Get all books

"""


class BooksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [IsAuthenticated, IsAdmin]

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            # permission_classes = [permissions.IsAdminUser,IsAdmin] # admin can  create retrive update delete only
            permission_classes = [IsAuthenticated | IsAdmin | IsAdminUser,
                                  DjangoModelPermissions]  # admin can  create retrive update delete only
        elif self.action == 'list':
            permission_classes = [
                IsAuthenticated| IsStudent | IsAdmin | IsAuthenticatedOrReadOnly | IsAdminUser | DjangoModelPermissions]  # only student books view.
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated| IsAdmin | IsAdminUser, DjangoModelPermissions]  # admin only
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated| IsAdmin | IsAdminUser, DjangoModelPermissions]  # admin only
        return [permission() for permission in permission_classes]
