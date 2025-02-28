from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration of movie in minutes")

    def __str__(self):
        return self.title


class Seat(models.Model):
    seat_number = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], unique=True)
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seat_number)


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField()

    class Meta:
        unique_together = ('seat', 'booking_date', 'user')
