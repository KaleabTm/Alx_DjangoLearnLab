from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from blog.models import Post
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
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})



class PostCreateView(LoginRequiredMixin, CreateView):
    class Meta:
        model = Post
        fields = '__all__'
        template_name = 'blog/post_form.html'

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

class PostListView(ListView):
    class Meta:
        model = Post
        fields = '__all__'
        template_name = 'blog/post_list.html'
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    class Meta:
        model = Post
        fields = ['title', 'content']
        template_name = 'blog/post_form.html'

        def form_valid(self, form):
            form.instance.author = self.request.user
            return super().form_valid(form)

        def test_func(self):
            post = self.get_object()
            return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    class Meta:
        model = Post
        success_url = '/'
        template_name = 'blog/post_confirm_delete.html'

        def test_func(self):
            post = self.get_object()
            return self.request.user == post.author


class PostDetailView(DetailView):
    class Meta:
        model = Post
        fields = '__all__'