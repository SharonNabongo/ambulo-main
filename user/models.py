from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
#from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, first_name, password, **other_fields):
        if not email:
            raise ValueError(_('You must provide an Email Address'))

        email=self.normalize_email(email)
        user = self.model(username=username, email=email,first_name=first_name, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)
        
        if other_fields.get('is_staff')is not True:
            raise ValueError('superuser must be set to is_staff=True')
        
        if other_fields.get('is_superuser')is not True:
            raise ValueError('superuser must be set to is_superuser=True')


        user = self.create_user(username, email, first_name, password, **other_fields)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    first_name =  models.CharField(max_length=200, blank=True)
    age = models.CharField(max_length=3, blank=True)
    gender = models.CharField(max_length= 10)
    phone = models.TextField(null=False, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name']
    
    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Message(models.Model):
    topic =  models.CharField(max_length=50)
    content = models.TextField()