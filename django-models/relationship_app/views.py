from django.shortcuts import redirect, render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth import logout
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


def check_role(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(lambda user: check_role(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(lambda user: check_role(user, 'Member'))
def member_view(request):
    return render(request, 'member_view.html')
