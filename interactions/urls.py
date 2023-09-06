from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "interactions"

urlpatterns = [
    path("playlists/", views.PlaylistsView.as_view(), name="playlists"),
    path("playlist/<int:pk>/", views.PlaylistView.as_view(), name="playlist"),
]
