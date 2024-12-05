# urls.py
from django.urls import path
from .views import Login, Logout, UserRegister, profile

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),  # Assuming you have a register view
    path('profile/', profile, name='profile'),  # User profile view
]
