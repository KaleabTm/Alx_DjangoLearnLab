from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import UserCreatetion
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import login

# Create your views here.
class Login(LoginView):
    template_name='blog/login.html'

class Logout(LogoutView):
    next_page='login/'


class UserRegister(CreateView):
    form_class = UserCreatetion  
    template_name = 'blog/register.html'  
    success_url = '/profile/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)
  


@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})