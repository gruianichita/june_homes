from django.urls import path

from june_homes.apps.users.views import LivingMarylandView

app_name = "users"

urlpatterns = [
    path("living-maryland/", LivingMarylandView.as_view(), name="living-maryland"),
]
