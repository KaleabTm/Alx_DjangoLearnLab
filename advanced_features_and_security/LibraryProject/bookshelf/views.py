from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required

from .forms import ExampleForm
from .models import Book
# Create your views here.

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
    return redirect('book_list')


@permission_required('bookshelf.can_view',raise_exception=True)
def view_book(request):
    book = get_object_or_404(Book, pk=id)
    return render("you have success fully retrieved a book")



