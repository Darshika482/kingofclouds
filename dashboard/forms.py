from django import forms
from .models import GalleryImage


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["description"]
