from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='movie_posters/')  
    background_poster = models.ImageField(upload_to='background_posters/', null=True, blank=True)

    def __str__(self):
        return self.title

class Trailer(models.Model):
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='trailers/posters/')
    video_url = models.URLField()

    def __str__(self):
        return self.title
