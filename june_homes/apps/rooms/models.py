from django.db import models

from june_homes.apps.hotels.models import Hotel


class Room(models.Model):
    title = models.CharField(max_length=128)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "room"
