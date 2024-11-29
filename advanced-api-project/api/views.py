from rest_framework import generics
from django_filters import rest_framework, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book
from rest_framework import mixins

class BookListView(mixins.ListModelMixin,generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend]
    filterset_fields = ['title','author','publication_year']
    filters.OrderingFilter = ['publication_year',]
    filters.SearchFilter = ['title','author']

class BookCreateView(mixins.CreateModelMixin,generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
class BookUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


    
