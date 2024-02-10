from django.urls import path
from . import views
from .views import index
from .views import delete_image
from .views import event_view

urlpatterns = [
    path("home/", views.index, name="home"),  # Homepage
    path("home/", views.index, name="homee"),  # Homepage
    path("event/", views.event, name="event"),  # Event page
    path("gallery/", views.gallery, name="gallery"),  # Gallery page
    path("delete_image/<int:image_id>/", delete_image, name="delete_image"),
    path("events/", views.event_view, name="event_view"),
]
