from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # ✅ for tags

# -----------------------------
# POST FORM
# -----------------------------
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include 'tags'
        widgets = {
            'tags': TagWidget(attrs={'class': 'form-control'}),  # ✅ TagWidget
        }

# -----------------------------
# COMMENT FORM
# -----------------------------
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add your comment...'})
        }
