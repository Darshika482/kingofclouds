from django import forms
from .models import GalleryImage
from .models import Event


# for gallery
class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ["description"]


# for event
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["name", "description", "event_date", "photo"]
