from django.urls import path
from . import views

urlpatterns = [
    path("", views.album, name="album"),
    path("add_media/", views.add_media, name="add_media"),
    path("edit_media/<int:media_id>/", views.edit_media, name="edit_media"),
    path(
        "delete_media/<int:media_id>/", views.delete_media, name="delete_media"
    ),
]
