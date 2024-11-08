from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

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



class UserRegisterView(CreateView):
    form = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = '/login/'

class UserLoginView(LoginView):
    form = AuthenticationForm()
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
