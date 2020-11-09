from django.contrib import admin
from .models import Event


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """
    Fields available in the admin, ordered by date
    """

    list_display = (
        "name",
        "venue",
        "programme",
        "date",
        "time",
        "event_url",
    )

    ordering = ("date",)


admin.site.register(Event, EventAdmin)
