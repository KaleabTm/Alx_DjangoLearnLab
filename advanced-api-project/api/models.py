from django.db import models

# Create your models here.


#This model holds the Authors name
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



#This model is for the books holding the title the writter and the year it was published
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    class Meta:
        filter = [
            'author',
            'title',
            'publication_year'
        ]
        ordering = ['publication_year',]

    def __str__(self):
        return f"{self.title} written by {self.author} and published on {self.publication_year}"




