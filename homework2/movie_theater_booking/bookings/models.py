from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import date, timedelta

def validate_seating_number(num):
    if num > 10:
        raise ValidationError("Seating Number must be within 1 - 10")
    elif num < 0:
        raise ValidationError("Seating Number must be within 1 - 10")

def validate_booking_date(user_date):
    if user_date < date.today():
        raise ValidationError("Booking must be today or 90 days into the future")
    elif user_date > date.today() + timedelta(days=90):
        raise ValidationError("Booking cannot be made more than 90 days ahead of time")


# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.PositiveIntegerField(help_text="Duration of movie in minutes")
    trailer_url = models.URLField(blank=True, null=True)
    poster = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"Title: {self.title} Description: {self.description} Release Date: {self.release_date} Duration: {self.duration}"


class Seat(models.Model):
    seat_number = models.SmallIntegerField(validators=[validate_seating_number], unique=True)
    booking_status = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat Number: {self.seat_number} Booking Status: {self.booking_status}"


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.PROTECT)
    seat = models.ForeignKey(Seat, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_date = models.DateField(default=now, validators=[validate_booking_date])

    class Meta:
        unique_together = ('seat', 'booking_date', 'user')
