from rest_framework import serializers
from .models import Author, Book

# This is a book serializer that serializes all the fields in the model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if len(data['title']) < 5:
            raise serializers.ValidationError("Title must be at least 5 characters long.")
        return data


# In this serializer we are seializing Auther and the related books that are written by him/her is included too
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name','books']
