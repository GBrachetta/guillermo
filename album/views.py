from django.shortcuts import render
from .models import Photo


# Create your views here.
def album(request):
    album = Photo.objects.all
    context = {
        "album": album,
    }
    return render(request, "album/album.html", context)
