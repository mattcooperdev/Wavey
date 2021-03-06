from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    '''Django DB model for profile creation '''
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                related_name='profile')
    profile_image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(max_length=800, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    social_youtube = models.URLField(max_length=200, blank=True, null=True)
    social_website = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user} Profile'
