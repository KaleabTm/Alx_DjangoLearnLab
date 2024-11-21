from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BookList(generics.ListAPIView):
    serializer_class=BookSerializer
    queryset=Book.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class=BookSerializer
    queryset=Book.objects.all()
