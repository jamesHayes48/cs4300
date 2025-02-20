from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.Charfield(max_length = 255)
    descrition = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help="Duration of movie in minutes")

class Seat