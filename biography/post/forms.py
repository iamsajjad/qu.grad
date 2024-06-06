
from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'url', 'image', 'text',)


class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ()

