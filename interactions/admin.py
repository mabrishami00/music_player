from django.contrib import admin
from .models import Comment, Playlist, Like

# Register your models here.

admin.site.register(Comment)
admin.site.register(Playlist)
admin.site.register(Like)
