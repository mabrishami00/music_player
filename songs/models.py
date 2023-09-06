from django.db import models
# from accounts.models import Band


class Genre(models.Model):
    name = models.CharField(max_length=50)

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    cover_photo = models.ImageField(upload_to="songs/cover_photos", default="default/icon_default.jpg")
    audio_file = models.FileField(upload_to="songs/audio_files")
    band = models.ForeignKey("accounts.Band", on_delete=models.CASCADE, null=True, blank=True)
    artists = models.ManyToManyField("accounts.Artist")
    genres = models.ManyToManyField(Genre)
