from django.shortcuts import render
from .models import Photo
from random import shuffle


def album(request):
    album = list(Photo.objects.all())
    shuffle(album)
    context = {"album": album, "media": "active"}
    return render(request, "album/album.html", context)
