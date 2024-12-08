# urls.py
from django.urls import path
from .views import Login, Logout, register, profile, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', register, name='register'),  
    path('profile/', profile, name='profile'),  
    path('post/', PostListView.as_view(), name='post-list'),  
    path('post/new/', PostCreateView.as_view(), name='post-create'),  
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),  
]
