from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import ProfileUpdateForm, UserCreatetion
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth import login

# Create your views here.
class Login(LoginView):
    template_name='blog/login.html'

class Logout(LogoutView):
    next_page='login/'


def register(request):
    if request.method == 'POST':
        form = UserCreatetion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreatetion()
    return render(request, 'auth/register.html', {'form': form})
  


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'auth/profile.html', {'form': form})