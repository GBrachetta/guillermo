from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Photo
from .forms import MediaForm


def album(request):
    """
    Renders the template with all objects in the Photo model.
    """

    album = Photo.objects.all()
    context = {"album": album, "media": "active"}
    return render(request, "album/album.html", context)


@login_required
def add_media(request):
    """
    Saves the form admins can fill out to add media to the gallery.
    If accessed directly from the address bar and not superuser, an
    error message shows in a toast and redirects to the album view.
    """
    if not request.user.is_superuser:
        messages.error(request, "Reserved to administrators.")
        return redirect(reverse("album"))

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
    context = {"form": form, "media": "active"}

    return render(request, template, context)


@login_required
def edit_media(request, media_id):
    """
    Same as above, takes media_id to effectively edit the intended item.
    """

    if not request.user.is_superuser:
        messages.error(request, "Reserved to administrators.")
        return redirect(reverse("album"))

    media = get_object_or_404(Photo, pk=media_id)

    if request.method == "POST":
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated media.")
            return redirect(reverse("album"))
        else:
            messages.error(request, "Failed to update. Please check the form.")
    else:
        form = MediaForm(instance=media)
        messages.info(request, "You are editing media.")

    template = "album/edit_media.html"
    context = {"form": form, "item": media, "media": "active"}

    return render(request, template, context)


@login_required
def delete_media(request, media_id):
    """
    Same as above, takes media_id to effectively delete the intended item.
    """
    if not request.user.is_superuser:
        messages.error(request, "Reserved to administrators.")
        return redirect(reverse("album"))
    media = get_object_or_404(Photo, pk=media_id)
    media.delete()
    messages.success(request, "Media deleted.")
    return redirect(reverse("album"))
