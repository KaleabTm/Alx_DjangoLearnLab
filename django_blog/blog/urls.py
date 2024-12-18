# urls.py
from django.urls import path
from .views import Login, Logout, register, profile, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, PostByTagListView


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', register, name='register'),  
    path('profile/', profile, name='profile'),  
    path('post/', PostListView.as_view(), name='post-list'),  
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-edit'),  
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', search_posts, name='search-posts'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts-by-tag')     
]
