from django.contrib import admin
from django.urls import path
from . import views

app_name = "songs"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("releases/", views.ReleasesView.as_view(), name="releases"),
    path("release/<int:pk>/", views.ReleaseView.as_view(), name="release"),
    path("artists/", views.ArtistsView.as_view(), name="artists"),
    path("artist/<int:pk>/", views.ArtistView.as_view(), name="artist"),
    path("like_unlike/<int:pk>/", views.LikeUnlikeSongView.as_view(), name="like_unlike"),
]
