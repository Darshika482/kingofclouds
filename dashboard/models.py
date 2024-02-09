from django.db import models


# Create your models here.


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery_images/")
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image {self.id} - {self.description[:20]}"


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateField()
    photo = models.ImageField(upload_to="events_photos/", null=True, blank=True)

    def __str__(self):
        return self.name
