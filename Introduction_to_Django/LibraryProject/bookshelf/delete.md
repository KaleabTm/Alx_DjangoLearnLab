from bookshelf.models import Book

# Delete the book instance
deleted = Book.objects.filter(title="Nineteen Eighty-Four").delete()
print(f"Deleted {deleted} book(s).")

# Confirm deletion by trying to retrieve all books
b = Book.objects.all()
print(list(all_books))
# Should return an empty list or no books
