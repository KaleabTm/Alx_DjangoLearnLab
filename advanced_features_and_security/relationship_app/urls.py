from django.urls import path
from .views import list_books, LibraryDetailView, register, LoginView, LogoutView
from .views import *
from . import views

url_patterns = [
    path('booklist/',list_books),
    path('librarydetail/', LibraryDetailView.as_view()),
    path('register/', views.register),
    path('admin/', admin_view),
    path('member/', member_view),
    path('librarian/',librarian_view),
    path('add_book/', add_book),
    path('deletebook/<int:id>',delete_book),
    path('edit_book/<int:id>',edit_book),
    path('login/', LoginView.as_view(template_name="relationship_app/login.html")),
    path('logout/', LogoutView.as_view(template_name="relationship_app/logout.html")),
]
