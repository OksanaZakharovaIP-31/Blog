from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for comment"""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    """Form for search"""
    query = forms.CharField()