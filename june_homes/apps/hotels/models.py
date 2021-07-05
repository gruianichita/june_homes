from django.db import models


class Hotel(models.Model):
    title = models.CharField(max_length=128)
    likes = models.PositiveIntegerField()
    dislikes = models.PositiveIntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "hotel"
