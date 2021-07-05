from django.db import models

class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE,
                             related_name='reservations')
start = models.DateField()
end = models.DateField()
user = models.ForeignKey(User, on_delete=models.CASCADE,
                         related_name='reservations')