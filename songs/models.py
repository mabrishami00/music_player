from django.db import models
from accounts.models import User, Artist, Band


class Genre(models.Model):
    name = models.CharField(max_length=50)

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to="/songs/cover_photos")
    audio_file = models.FileField(upload_to="/songs/audio_files")
    band = models.ForeignKey(Band, on_delete=models.CASCADE, null=True, blank=True)
    genres = models.ManyToManyField(Genre)