from django.contrib import admin
from .models import GalleryImage


class GalleryAdmin(admin.ModelAdmin):
    list_display = ("image", "description")


# Register your models here.
admin.site.register(GalleryImage, GalleryAdmin)
