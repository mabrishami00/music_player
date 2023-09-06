from django.shortcuts import render
from django.views import View
from .models import Playlist
from songs.models import Song
from .forms import AddPlaylistForm

# Create your views here.
class PlaylistView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        playlist = Playlist.objects.get(pk=kwargs["pk"], user=user)
        context = {"playlist": playlist}
        return render(request, "interactions/playlist.html", context=context)

    def post(self, request, *args, **kwargs):
        pass


class PlaylistsView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        playlists = Playlist.objects.filter(user=user).order_by("created_at")
        context = {"playlists": playlists}
        return render(request, "interactions/playlists.html", context=context)

    # def post(self, request, *args, **kwargs):
    #     Playlist.objects.create(user=request.user,)


class AddPlaylistsView(View):
    form_class = AddPlaylistForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        songs = Song.objects.all().order_by("created_at")
        context = {"songs": songs, "form": form}
        return render(request, "songs/add_playlist.html", context=context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Playlist.objects.create(
                user=request.user, name=cd["name"], description=cd["description"]
            )
