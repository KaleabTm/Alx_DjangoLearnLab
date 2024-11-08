from django.urls import path
from .views import list_books, LibraryDetailView, UserRegisterView, login_view, UserLogoutView

url_patterns = [
    path('booklist/',list_books),
    path('librarydetail/', LibraryDetailView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('login/', login_view),
    path('logout/', UserLogoutView.as_view()),
]