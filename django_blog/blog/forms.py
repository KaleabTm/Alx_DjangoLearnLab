from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User


class UserCreatetion(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta: 
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
