from django.shortcuts import render

from django.views.generic import ListView
from .models import Post

class PostList(ListView):
    model = Post
    context_object_name = 'my_favorite_publishers'
    template_name = 'posts_list.html'
