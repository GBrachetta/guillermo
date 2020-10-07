from django.contrib import admin
from .models import Cd


# Register your models here.
class CdAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Cd, CdAdmin)
