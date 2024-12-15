from django.db import models
from django.contrib.auth.models import AbstractUser
from .user_manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=200)
    bio = models.CharField(max_length=200)
    profile_picture = models.BinaryField(blank=True, null=True)
    followers = models.ManyToManyField('self',symmetrical=False)
    username=None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS=[]

    objects=CustomUserManager()

    def __str__(self):
        return f"{self.first_name} - {self.last_name}"

