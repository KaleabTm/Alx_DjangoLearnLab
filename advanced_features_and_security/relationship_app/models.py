from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

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

# Create your models here.
class Author(User):
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete= models.PROTECT)
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_delete_book', 'Can delete book'),
            ('can_change_book', 'Can change book')
        ]

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Librarian(User):
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username - self.role
