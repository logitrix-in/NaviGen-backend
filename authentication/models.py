from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='upload/profile_pictures/', null=True, blank=True)
    user_permissions = None
    groups = None
