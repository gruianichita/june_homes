from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=128)
hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,
                          related_name='rooms')
