from rest_framework import serializers
from .models import Author, Book

# This is a book serializer that serializes all the fields in the model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



# In this serializer we are seializing Auther and the related books that are written by him/her is included too
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = ['name','books']
