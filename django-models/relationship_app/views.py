from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic import DetailView


# Create your views here.
def list_book(request):
    book = Book.objects.all()
    context = {
        'book':book
    }
    return render(request, template_name='relationship_app/list_books.html', context=context)

class LibraryDetail(DetailView):
    model = Library
    template_name='relationship_app/library_detail.html'
    context_object_name = 'library'  