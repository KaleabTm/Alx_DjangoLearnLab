from django import forms
from .models import Book  # Import the Book model

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']  # Include the fields you want to capture

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3:
            raise forms.ValidationError("The title must be at least 3 characters long.")
        return title

    def clean_author(self):
        author = self.cleaned_data.get('author')
        if not author.isalpha():
            raise forms.ValidationError("Author name must contain only alphabetic characters.")
        return author
