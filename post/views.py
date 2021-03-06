from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Post

class PostList(ListView):
    model = Post
    #context_object_name = 'my_favorite_publishers'



class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['post_list'] = Post.objects.all()
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['subject', 'content']
    success_url = '/post'
    #success_url = reverse_lazy('post_list')


class PostUpdate(UpdateView):
    model = Post
    fields = ['subject', 'content']
