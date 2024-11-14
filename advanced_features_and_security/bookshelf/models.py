from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

class UserManager(UserManager):
    def create_user(self, name, password):

        if not name:
            raise ValueError("pleals insert your name")
        if not password:
            raise ValueError("please insert your password")
        
        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self.__db)

        return user
    

    def create_superuser(self,name,password):

        user=self.create_user(name,password)
        user.is_stuff=True
        user.is_superuser=True
        user.save(using=self._db)

        return user


    
class User(AbstractUser):
    name = models.CharField(unique=True, max_length=100)
    date_of_birth= models.DateField()
    profile_photo= models.ImageField()

    objects=UserManager()

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []