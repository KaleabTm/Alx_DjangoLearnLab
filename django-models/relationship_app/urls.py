from django.urls import path
from .views import list_books, LibraryDetailView

url_patterns = [
    path('booklist/',list_books),
    path('librarydetail/', LibraryDetailView.as_view())
]