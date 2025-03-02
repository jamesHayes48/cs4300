from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration of movie in minutes")
    trailer_url = models.URLField(blank=True, null=True)
    poster = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Seat(models.Model):
    seat_number = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], unique=True)
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.seat_number)


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_date = models.DateField(default=now)

    class Meta:
        unique_together = ('seat', 'booking_date', 'user')
