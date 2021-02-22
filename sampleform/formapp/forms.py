
from django import forms
from .models import Post

# modelの中のPostを参照してデータベースと繋ぐ

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'memo')





















