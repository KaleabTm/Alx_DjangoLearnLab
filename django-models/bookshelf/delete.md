from bookshelf.models import Book

# Delete the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")
# Delete the book instance
book.delete()  # Delete the book
print("Book deleted successfully.")

# Confirm deletion by trying to retrieve all books
b = Book.objects.all()
print(list(all_books))
# Should return an empty list or no books
