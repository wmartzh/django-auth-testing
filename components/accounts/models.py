from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import BCryptPasswordHasher
# Create your models here.



class UserManager(BaseUserManager):

    def create_user(self,username,email,password, **extra_fields):

        if not email:
            raise ValueError("User must have an email address")
        if not password:
            raise ValueError("User must have a password")
        email = self.normalize_email(email)
        user = self.model(username=username,email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,email,password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(('Superuser must have is_superuser=True.'))
        return self.create_user(username,email, password, **extra_fields)



class User(AbstractUser):
    objects = UserManager()
    
    email       = models.EmailField(max_length=255, unique=True)
    first_name  = models.CharField(max_length=12)
    last_name   = models.CharField(max_length=12)
    username    = models.CharField(max_length=15, unique=True)
    is_active      = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=False)
    is_admin       = models.BooleanField(default=False)
    is_superuser   = models.BooleanField(default=False)
    timestamp   = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email','password']

    

    def __str__(self):
        return self.username
