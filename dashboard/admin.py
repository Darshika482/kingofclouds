from django.contrib import admin
from .models import GalleryImage, Event


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("image", "description")


# for event model display
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "event_date", "photo")


# Register your models here.
admin.site.register(GalleryImage, GalleryAdmin)
admin.site.register(Event, EventAdmin)
