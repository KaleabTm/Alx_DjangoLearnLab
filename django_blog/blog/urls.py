# urls.py
from django.urls import path
from .views import Login, Logout, register, profile, PostCreateView, PostDeleteView, PostDetailView, PostListView, PostUpdateView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', register, name='register'),  
    path('profile/', profile, name='profile'),  
    path('create/', PostCreateView.as_view(), name='post-create'),  
    path('list/', PostListView.as_view(), name='post-list'),  
    path('detail/<int:id>/', PostDetailView.as_view(), name='post-detail'),  
    path('delete/<int:id>/', PostDeleteView.as_view(), name='post-delete'),  
    path('update/<int:id>/', PostUpdateView.as_view(), name='post-update'),  
]
