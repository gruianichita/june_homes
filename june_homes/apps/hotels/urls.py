from django.urls import path

from june_homes.apps.hotels import views

app_name = "hotels"

urlpatterns = [
    path("like/<int:hotel_id>", views.like_hotel_view, name="like"),
    path("dislike/<int:hotel_id>", views.dislike_hotel_view, name="dislike"),
    path("free-rooms/", views.HotelsWithFreeRoomsView.as_view(), name="free-rooms")
]
