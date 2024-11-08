from django.shortcuts import redirect, render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test



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


@user_passes_test(is_admin)
def admin(request):
    return ('This user is admin')


@user_passes_test(is_librarian)
def librarian(request):
    return ('This user is librarian')



@user_passes_test(is_member)
def member(request):
    return ('This user is member')

