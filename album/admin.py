from django.contrib import admin
from .models import Photo


class PhotoAdmin(admin.ModelAdmin):
    """
    Fields displayed in admin.
    Allows to display a thumbnail of the images in the admin.
    """

    list_display = (
        "name",
        "caption",
        "image_url",
        "image",
        "thumbnail_preview",
    )
    readonly_fields = ("thumbnail_preview",)

    ordering = ("name",)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = "Thumbnail Preview"
    thumbnail_preview.allow_tags = True


admin.site.register(Photo, PhotoAdmin)
