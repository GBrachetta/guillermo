from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "venue",
        "description",
        "date",
        "time",
        "event_url",
        "image",
        "image_url",
        "thumbnail_preview",
    )
    readonly_fields = ("thumbnail_preview",)

    ordering = ("date",)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = "Thumbnail Preview"
    thumbnail_preview.allow_tags = True


admin.site.register(Event, EventAdmin)
