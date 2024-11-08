from django.shortcuts import render
from .models import Book, Librarian,Library, Author
from django.views.generic import DetailView


# Create your views here.
def list_book(request):
    book = Book.objects.all()
    context = {
        'book':book
    }
    return render(request,template_name='list_book.html', context=context)

class LibraryDetail(DetailView):
    model = Library
    template_name='library_detail.html'
    context_object_name = 'library'  