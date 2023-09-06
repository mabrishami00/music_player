from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import Song
from accounts.models import Artist
from .forms import CommentForm
from interactions.models import Comment, Like
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class HomeView(View):
    def get(self, request):
        songs = Song.objects.all().order_by("created_at")
        artists = Artist.objects.all().order_by("joined")
        song = songs.last()
        context = {"songs": songs, "song": song, "artists": artists}
        return render(request, "songs/index.html", context=context)


class ReleasesView(View):
    def get(self, request, *args, **kwargs):
        songs = Song.objects.all().order_by("created_at")
        context = {"songs": songs}
        return render(request, "songs/releases.html", context=context)


class ReleaseView(View):
    form_class = CommentForm

    def get(self, request, *args, **kwargs):
        song = Song.objects.get(pk=kwargs["pk"])
        user = request.user
        liked = Like.objects.filter(user=user, song=song).exists()
        number_of_likes = song.like_set.all().count()
        form = self.form_class
        context = {"song": song, "form": form, "liked": liked, "number_of_likes": number_of_likes}
        return render(request, "songs/release.html", context=context)

    def post(self, request, *args, **kwargs):
        if "submit_new" in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                body = cd["body"]
                user = request.user
                song = Song.objects.get(pk=kwargs["pk"])
                Comment.objects.create(body=body, user=user, song=song)
                return redirect("songs:release", song.pk)

        if "submit_reply" in request.POST:
            form = self.form_class(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                body = cd["body"]
                comment_id = request.POST.get("comment_id")
                parent_comment = Comment.objects.get(pk=comment_id)
                user = request.user
                song = Song.objects.get(pk=kwargs["pk"])
                Comment.objects.create(
                    body=body,
                    user=user,
                    song=song,
                    comment_reply=parent_comment,
                    is_reply=True,
                )
                return redirect("songs:release", song.pk)


class ArtistsView(View):
    def get(self, request, *args, **kwargs):
        artists = Artist.objects.all().order_by("joined")
        context = {"artists": artists}
        return render(request, "songs/artists.html", context=context)


class ArtistView(View):
    def get(self, request, *args, **kwargs):
        artist = Artist.objects.get(pk=kwargs["pk"])
        context = {"artist": artist}
        return render(request, "songs/artist.html", context=context)


class LikeUnlikeSongView(LoginRequiredMixin, View):
    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        self.user = request.user
        self.song = Song.objects.get(pk=kwargs["pk"])
        self.liked = Like.objects.filter(user=self.user, song=self.song).exists()
    
    def post(self, request, *args, **kwargs):
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:          
            if self.liked:
                Like.objects.filter(user=self.user, song=self.song).delete()
            else:
                Like.objects.create(user=self.user, song=self.song)
            number_of_likes = self.song.like_set.all().count()
            liked = Like.objects.filter(user=self.user, song=self.song).exists()
            data = {'number_of_likes': number_of_likes, 'liked':liked, "message": "successful"}
            return JsonResponse(data)

