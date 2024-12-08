from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import ProfileUpdateForm, UserCreatetion, CommentForm
from django.contrib.auth.views import LoginView, LogoutView 
from django.db.models import Q
from taggit.models import Tag
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



@login_required
class CommentCreateView(CreateView):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.author = request.user
                comment.save()
                return redirect('post-detail', pk=post_id)
        else:
            form = CommentForm()
        return render(request, 'blog/comment_form.html', {'form': form})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.all()
    if query:
        results = results.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    return render(request, 'blog/post_list.html', {'results': results, 'query': query})

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, 'blog/posts_by_tag.html', {'tag': tag, 'posts': posts})
