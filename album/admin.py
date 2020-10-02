from django.contrib import admin
from .models import Album


# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
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


admin.site.register(Album, AlbumAdmin)
