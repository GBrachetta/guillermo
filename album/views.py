from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Photo
from random import shuffle
from .forms import MediaForm


def album(request):
    album = list(Photo.objects.all())
    shuffle(album)
    context = {"album": album, "media": "active"}
    return render(request, "album/album.html", context)


def add_media(request):
    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Media added.")
            return redirect(reverse("album"))
        else:
            messages.error(
                request, "Failed to add media. Please check the form."
            )
    else:
        form = MediaForm()

    template = "album/add_media.html"
    context = {"form": form}

    return render(request, template, context)


def edit_media(request, media_id):
    media = get_object_or_404(Photo, pk=media_id)

    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated media.")
            return redirect(reverse("edit_media", args=[media.id]))
        else:
            messages.error(request, "Failed to update. Please check the form.")
    else:
        form = MediaForm(instance=media)
        messages.info(request, "You are editing media.")

    template = "album/edit_media.html"
    context = {"form": form, "media": media}

    return render(request, template, context)


def delete_media(request, media_id):
    media = get_object_or_404(Photo, pk=media_id)
    media.delete()
    messages.success(request, "Media deleted.")
    return redirect(reverse("album"))
