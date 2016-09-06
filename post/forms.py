from django import forms
from pagedown.widgets import PagedownWidget
from .models import Post

class PostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget)
    model = Post
    exclude = ('create_at','modify' )
