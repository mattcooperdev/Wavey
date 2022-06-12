from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


# Can set to draft for admin to control posting
# Of articles and comments
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    '''
    Database model for Posts.
    '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts'
    )
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=1)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        '''
        Decides ordering of posts from
        most recent first
        '''
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        '''
        Shows count of likes added to post
        '''
        return self.likes.count()

    def get_absolute_url(self):
        '''
        Will return successful post
        to related slug url
        '''
        return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.strip().replace(' ', '-')
        super().save(*args, **kwargs)


class Comment(models.Model):
    '''
    Database model for comments.
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE,
        related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        '''
        Decides ordering of comments from
        oldest first
        '''
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
