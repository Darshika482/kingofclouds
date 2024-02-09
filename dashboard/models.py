from django.db import models


# Create your models here.


class GalleryImage(models.Model):
    image = models.ImageField(upload_to="gallery_images/")
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image {self.id} - {self.description[:20]}"
