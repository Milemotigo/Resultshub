from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=255)

class collegeUser(CustomUser):
    # Add your additional fields her
    POBox_PMB = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    date_founded = models.DateField(null=True, blank=True)
    
