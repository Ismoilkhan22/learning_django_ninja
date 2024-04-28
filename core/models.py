from django.db import models


class Tract(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=250)
    duration = models.FloatField()
    last_display = models.DateTimeField()

