from django.views.generic import ListView, DetailView
from .models import Post

# Class based view for all the posts in a list formate
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

# Class based view for specific blog posts 
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

