from django.urls import path

from june_homes.apps.rooms import views

app_name = "rooms"

urlpatterns = [
    path("sold-out/", views.SoldOutView.as_view(), name="sold-out")
]
