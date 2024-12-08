# urls.py
from django.urls import path
from .views import Login, Logout, register, profile, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView, add_comment, CommentUpdateView, CommentDeleteView,

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
    path('posts/<int:post_id>/comments/new/', add_comment, name='comment-add'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
     
]
