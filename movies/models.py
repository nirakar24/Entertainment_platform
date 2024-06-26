from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movie_posters/')  
    background_poster = models.ImageField(upload_to='background_posters/', null=True, blank=True)
    trailer = models.ForeignKey('Trailer', on_delete=models.SET_NULL, null=True, blank=True)
    streaming_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Trailer(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='trailers/posters/')
    video_url = models.URLField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wishlist = models.ManyToManyField(Movie, blank=True)

    def __str__(self):
        return self.user.username
