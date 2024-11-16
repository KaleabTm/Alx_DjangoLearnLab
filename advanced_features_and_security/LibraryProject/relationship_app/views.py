from django.shortcuts import get_object_or_404, redirect, render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
# Create your views here.
def list_books(request):
    book = Book.objects.all()
    context = {
        'book':book
    }
    return render(request, template_name='relationship_app/list_books.html', context=context)

class LibraryDetailView(DetailView):
    model = Library
    template_name='relationship_app/library_detail.html'
    context_object_name = 'library' 

@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
        

class LoginView(LoginView):
    def login_view(request):
        if request.method == "POST":
           form = AuthenticationForm(request, data=request.POST)
           if form.is_valid():
               login(request, form.get_user())
               return redirect('register')
           else:
               form = AuthenticationForm()
        return render(request, {'form': form})
        

class LogoutView(LogoutView):
    def logout_view(request):
        logout(request)
        return redirect('register')
    


def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


@csrf_exempt
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@csrf_exempt
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


@csrf_exempt
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@csrf_exempt
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        book = Book.objects.create(title=title, author=author)
        book.save()
    return redirect('book_list')


@csrf_exempt
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request,id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')


@csrf_exempt
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request):
    book = get_object_or_404(Book, pk=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.save()
    return redirect('book_list')


