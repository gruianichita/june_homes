from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("june_homes.apps.users.urls", namespace="users")),
    path("hotels/", include("june_homes.apps.hotels.urls", namespace="hotels")),
    # path("reservations/", include("june_homes.apps.reservations.urls", namespace="reservations")),
    path("rooms/", include("june_homes.apps.rooms.urls", namespace="rooms")),

]
