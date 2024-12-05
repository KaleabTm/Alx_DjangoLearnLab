# urls.py
from django.urls import path
from .views import Login, Logout, register, profile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', register, name='register'),  
    path('profile/', profile, name='profile'),  
]
