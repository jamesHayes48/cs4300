from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    descrition = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration of movie in minutes")


class Seat(models.Model):
    seat_number = models.CharField(max_length=3, unique=True)
    booking_status = models.BooleanField(default=False)


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()