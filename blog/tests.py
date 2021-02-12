from django.contrib.auth import get_user_model
from django.urls import reverse 
from django.test import TestCase


from .models import Post

# Create a Class to tests the Blogs app
class BlogTests(TestCase):
    # Create a setup Function
    def setUp(self):
        # Create a test user 
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'test@email.com',
            password = 'secret'
        )
        
        # Create a test Post 
        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author = self.user,
        )

    # Function to test string representations of posts 
    def test_string_representations(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)
    
    # Function to test if the model returns the absolute url properly 
    def test_get_absolute_url(self): 
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    # Function to test post content 
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body content')
    
    # Function to test listing posts view
    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body content')
        self.assertTemplateUsed(response, 'home.html')

    # Function to test detail posts view 
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')
    
    # Function to test create post view
    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'New title',
            'body': 'New text',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'New title')
        self.assertEqual(Post.objects.last().body, 'New text')

    # Function to test update post view
    def test_post_udate_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, 302)

    # Function to test post delete view
    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)


    
