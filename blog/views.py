from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy 
from .models import Post

# Class based view for all the posts in a list formate
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# Class based view for specific blog posts 
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# Class based view for creating new blog posts 
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

# Class based view for editing blog posts
class BlogUpdateView(UpdateView):
    model = Post 
    template_name = 'post_edit.html'
    fields = ['title', 'body']

# Class based view for deleting blog posts
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
