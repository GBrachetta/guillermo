import os
import uuid
from django.db import models
from django.utils.html import mark_safe


def random_filename(instance, filename):
    """
    Returns a random filename to avoid name duplicates when uploading media.
    """

    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("", filename)


class Photo(models.Model):
    """
    The photo model renders a thumbnail of the media it contains.
    """

    name = models.CharField(max_length=254)
    caption = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to=random_filename, null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe(
                '<img src="{}" width="100" height="100" />'.format(
                    self.image.url
                )
            )
        return ""

    def __str__(self):
        return self.name
