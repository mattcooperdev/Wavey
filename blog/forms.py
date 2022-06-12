from tinymce.widgets import TinyMCE
from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    '''
    Form for posting comment
    '''
    class Meta:
        model = Comment
        fields = ['body']


class PostForm(forms.ModelForm):
    '''
    Form for creating post
    '''
    class Meta:
        '''
        Introduce TinyMCE to content field
        of post form and other fields from Post model
        '''
        model = Post
        content = forms.CharField(
            widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
        fields = [
            'title',
            'excerpt',
            'featured_image',
            'content'
        ]
