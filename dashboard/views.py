from django.shortcuts import render, redirect
from maintest.models import Booking
from .forms import ImageUploadForm
from .models import GalleryImage
from django.contrib import messages


# added for gallery
from django.http import HttpResponseRedirect
from django.urls import reverse


# Home page view
def index(request):
    bookings = Booking.objects.all()
    return render(request, "dashboard/index.html", {"bookings": bookings})


# Event page view
def event(request):
    return render(request, "dashboard/event.html")


# Gallery page view
def gallery(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST)
        files = request.FILES.getlist(
            "image_files"
        )  # 'image_files' corresponds to the input name in HTML
        if form.is_valid():
            description = form.cleaned_data.get("description")
            for f in files:
                GalleryImage.objects.create(image=f, description=description)
            messages.success(request, "Images uploaded successfully.")
            return redirect("gallery")
    else:
        form = ImageUploadForm()
    images = GalleryImage.objects.all()
    return render(request, "dashboard/gallery.html", {"form": form, "images": images})


def index(request):
    bookings = Booking.objects.all()
    return render(request, "dashboard/index.html", {"bookings": bookings})


# added for gallery
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import GalleryImage
from django.contrib import messages  # Import the messages framework


def delete_image(request, image_id):
    image = GalleryImage.objects.get(id=image_id)
    image.delete()
    messages.success(request, "Image deleted successfully.")  # Add a success message
    return HttpResponseRedirect(reverse("gallery"))


# imported for event section

from .models import Event
from .forms import EventForm


def event_view(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("event_view")
    else:
        form = EventForm()
    events = Event.objects.all()
    return render(request, "dashboard/event.html", {"form": form, "events": events})
