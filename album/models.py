import os
import uuid
from django.db import models
from django.utils.html import mark_safe
from .make_thumbnail import make_thumbnail
from django.core.validators import FileExtensionValidator


def random_filename(instance, filename):
    """
    Returns a random filename to avoid name duplicates when uploading media.
    """

    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("", filename)


class Photo(models.Model):
    """
    If image is present and has a valid format, generates its thumbnail.
    Otherwise it's an url and skips that method.
    """

    name = models.CharField(max_length=254)
    caption = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        upload_to=random_filename,
        null=True,
        blank=True,
        validators=[FileExtensionValidator(["jpeg", "jpg", "png"])],
    )
    thumbnail = models.ImageField(
        upload_to=random_filename, null=True, blank=True
    )

    def save(self, *args, **kwargs):
        if self.image:
            self.thumbnail = make_thumbnail(self.image, size=(600, 600))

            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)

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
