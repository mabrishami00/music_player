from django.db import models
from accounts.models import User
from songs.models import Song


class Playlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to="playlists/cover_photo", default="default/icon_default.jpg")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    songs = models.ManyToManyField(Song)
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_reply = models.ForeignKey(
        "self",
        related_name="comments_reply",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    body = models.TextField()
    is_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)
