from django.contrib.auth.models import UserManager
from rest_framework.response import Response
from rest_framework import status


class CustomUserManager(UserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            return Response("Please enter an email!", status=status.HTTP_400_BAD_REQUEST)
        
        email = self.normalize_email(email)
        user=self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_staff=True
        user.is_superuser=True

        user.save(using=self._db)

        return user
        

        