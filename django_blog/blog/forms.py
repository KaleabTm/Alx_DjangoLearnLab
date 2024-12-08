from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .models import Post


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


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author','published_date']

        def clean_title(self):
            if not self.title:
                raise forms.ValidationError("title could not be empty")
            
        def clean_content(self):
            if not self.content:
                raise forms.ValidationError("content could not be empty")
            
