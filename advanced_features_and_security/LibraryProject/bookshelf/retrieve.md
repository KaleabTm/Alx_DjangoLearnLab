from bookshelf.models import Book

# Retrieve and display all attributes of the book
b = Book.objects.get(title="1984")
print(b.title,b.author,b.publication_year)

