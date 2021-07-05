from django.db import models

class Hotel(models.Model):
    title = models.CharField(max_length=128) 
    likes = models.PositiveIntegerField() 
    dislikes = models.PositiveIntegerField()
