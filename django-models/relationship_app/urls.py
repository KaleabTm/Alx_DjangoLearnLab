from django.urls import path
from .views import list_book, LibraryDetail

url_patterns = [
    path('booklist/',list_book),
    path('librarydetail/', LibraryDetail.as_view())
]