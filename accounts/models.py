from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must have staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have superuser=True')
        return self.create_user(email, user_name, password, **other_fields)

    def create_user(self, email, user_name, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class AllUsers(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    user_name = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(default=timezone.now)
    about = models.TextField(max_length=500, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    GENDER_CHOICES = (
        ('Not Selected', 'Not Selected'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='Not Selected')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name',]

    objects = CustomAccountManager()

    def __str__(self):
        return self.user_name