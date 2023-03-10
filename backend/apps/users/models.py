from django.db import models
from django.contrib.auth.models import\
    AbstractBaseUser, PermissionsMixin
from common.mixins.models import UUIDModel
from .managers import UserManager


class User(UUIDModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,
                              unique=True,
                              db_index=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    
    objects = UserManager()

    def __str__(self) -> str:
        return self.username
