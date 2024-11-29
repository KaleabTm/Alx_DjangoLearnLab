from django.urls import path
from .views import BookCreateView, BookDetailView, BookListView, BookDeleteView, BookUpdateView


urlpatterns = [
    path('books/', BookListView.as_view(), name='books-list'),
    path('books/create', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name='book-delete'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
]
