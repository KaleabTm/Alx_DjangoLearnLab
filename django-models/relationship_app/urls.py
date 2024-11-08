from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView, admin, member, librarian
from .views import *


url_patterns = [
    path('booklist/',list_books),
    path('librarydetail/', LibraryDetailView.as_view()),
    path('register/', register),
    path('admin/', admin),
    path('member/', member),
    path('librarian/',librarian),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html")),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html")),
]

# "views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="