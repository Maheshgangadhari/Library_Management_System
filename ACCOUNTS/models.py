from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    """ custom user model """

    USER = [
        ('select', _('SELECT')),
        ('admin', _('ADMIN USER')),
        ('student', _('STUDENT USER'))
    ]

    username = None
    first_name = None
    last_name = None
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True)
    
    type = models.CharField(max_length=50, choices=USER,default='select')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name',]

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def create_user(self):
        pass

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        ordering = ['-date_joined']

