from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Artist(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    youtube_video_id = models.CharField(max_length=100, null=True) 

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ArtistDetail', kwargs={'pk':self.pk})


class YouTubeLink(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.title
    
    def video_id(self):
        # Extract video ID from YouTube URL
        url_parts = self.link.split("?v=")
        if len(url_parts) > 1:
            return url_parts[1]
        else:
            # If the URL format is different, you may need to handle it differently
            return None
    
class UserProfile(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='users/', null=True, blank=True)

    def __str__(self):
        return self.user_name
    
    def get_absolute_url(self):
        return reverse('UserProfileDetail', kwargs={'pk':self.pk})

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='orders')

    def __str__(self):
        return f'Order {self.pk} by {self.user.username}'

    def get_absolute_url(self):
        return reverse('order_detail', kwargs={'pk': self.pk})
