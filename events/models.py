from django.db import models
from django.utils.html import mark_safe
from datetime import date


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    venue = models.CharField(max_length=254, null=False, blank=False)
    programme = models.TextField(null=False, blank=False)
    date = models.DateField(auto_now_add=False, null=False, blank=False)
    time = models.TimeField(auto_now_add=False, null=False, blank=False)
    event_url = models.URLField(max_length=1024, null=True, blank=True)

    @property
    def is_due(self):
        return date.today() > self.date

    @property
    def is_future(self):
        return date.today() <= self.date

    def __str__(self):
        return self.name
