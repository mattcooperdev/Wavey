from .models import Comment, Post
from django import forms
from tinymce.widgets import TinyMCE


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        fields = [
            'title',
            'excerpt',
            'featured_image',
            'content'
        ]
