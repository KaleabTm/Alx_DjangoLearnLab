from django.urls import path
from .views import list_book, LibraryDetailView

url_patterns = [
    path('booklist/',list_book),
    path('librarydetail/', LibraryDetailView.as_view())
]