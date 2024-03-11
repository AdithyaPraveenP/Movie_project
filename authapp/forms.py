from django import forms
from .models import AddMovie
from .models import Comment


class MovieForm(forms.ModelForm):
    class Meta:
        model = AddMovie
        fields = ['title', 'release', 'description', 'movie_length', 'cover', 'genre']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['text']