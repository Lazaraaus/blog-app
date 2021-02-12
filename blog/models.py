from django.db import models
from django.urls import reverse

# Create a Post class to model a post on our Blog app 
class Post(models.Model):
    # Create a field for a title 
    title = models.CharField(max_length=200)
    
    # Create a field for the author 
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        
    )

    # Create a field for the body
    body = models.TextField()

    # Custom str Function to display title 
    def __str__(self):
        return self.title 
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
