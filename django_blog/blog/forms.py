from taggit.forms import TagWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from .models import Post, Comment


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
        fields = ['title', 'content', 'author', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

        def clean_title(self):
            if not self.title:
                raise forms.ValidationError("title could not be empty")
            
        def clean_content(self):
            if not self.content:
                raise forms.ValidationError("content could not be empty")
            


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }