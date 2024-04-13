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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ArtistDetail', kwargs={'pk':self.pk})
    
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
