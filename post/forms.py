from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):
    model = Post
    exclude = ('create_at','modify' )
