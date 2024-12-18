from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ("can_view","Can View Books" ),
            ("can_create","Can Create Books"), 
            ("can_edit", "Can Edit Books"),
            ("can_delete", "Can Delete Books"),
        ]

class CustomUserManager(BaseUserManager):
    def create_user(self, name, password):

        if not name:
            raise ValueError("pleals insert your name")
        if not password:
            raise ValueError("please insert your password")
        
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    

    def create_superuser(self,name,password):

        user=self.create_user(name,password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user


    
class CustomUser(AbstractUser):
    name = models.CharField(unique=True, max_length=100)
    date_of_birth= models.DateField(null=True)
    profile_photo= models.ImageField(null=True)

    objects=CustomUserManager()

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []