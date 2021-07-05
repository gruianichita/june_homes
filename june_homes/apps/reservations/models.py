from django.contrib.auth.models import User
from django.db import models

from june_homes.apps.rooms.models import Room


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    start = models.DateField()
    end = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')

    objects = models.Manager()
    
    def __str__(self):
        return " ".join((self.room.title, self.user.username))

    class Meta:
        db_table = "reservation"
