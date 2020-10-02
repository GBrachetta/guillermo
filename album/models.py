from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=254)
    caption = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

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
