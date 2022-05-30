from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    '''Django DB model for profile creation '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    profile_image = CloudinaryField('image', default='')
    bio = models.TextField(max_length=800, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    social_youtube = models.URLField(max_length=200, blank=True, null=True)
    social_website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
