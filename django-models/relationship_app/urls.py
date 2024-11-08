from django.urls import path
from .views import list_books, LibraryDetailView, UserRegisterView, UserLoginView, UserLogoutView

url_patterns = [
    path('booklist/',list_books),
    path('librarydetail/', LibraryDetailView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
]