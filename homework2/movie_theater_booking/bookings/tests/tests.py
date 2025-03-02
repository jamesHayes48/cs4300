from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
from datetime import date

# Create your tests here.
class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="Movie1", description="xyz",
            release_date=date(2003, 11, 11), duration=120)

    def test_movie_creation(self):
        movie_1 = Movie.objects.get(title="Movie1")
        self.assertEqual(movie_1.title, "Movie1")
        self.assertEqual(movie_1.description, "xyz")
        self.assertEqual(movie_1.release_date, date(2003, 11, 11))
        self.assertEqual(movie_1.duration, 120)

class SeatTestCase(TestCase):
    def setUp(self):
        Seat.objects.create(seat_number=12)

    def test_seat_creation(self):
        seat_12 = Seat.objects.get(seat_number=12)
        self.assertEqual(seat_12.seat_number, 12)
        self.assertEqual(seat_12.booking_status, False)

class BookingTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="Movie1", description="xyz",
            release_date=date(2003, 11, 11), duration=120)
        Seat.objects.create(seat_number=12)
        User.objects.create_user(username="test", password="test")
        Booking.objects.create(movie=Movie.objects.get(title="Movie1"),seat=Seat.objects.get(seat_number=12), 
            user=User.objects.get(username="test"))

    def test_booking_creation(self):
        movie_1 = Movie.objects.get(title="Movie1")
        seat_12 = Seat.objects.get(seat_number=12)
        user_1 = User.objects.get(username="test")
        booking_1 = Booking.objects.get(movie=movie_1, seat=seat_12, user=user_1)
        
        # Test booking ties with movie object
        self.assertEqual(booking_1.movie.title, "Movie1")
        self.assertEqual(booking_1.movie.description, "xyz")
        self.assertEqual(booking_1.movie.release_date, date(2003, 11, 11))
        self.assertEqual(booking_1.movie.duration, 120)

        # Test booking ties with seat object
        self.assertEqual(booking_1.seat.seat_number, 12)
        # This setting is set to true for the book_seat function in views.py
        self.assertEqual(booking_1.seat.booking_status, False)

        # Test that another object cannot be created with the unique fields
        with self.assertRaises(IntegrityError):
            Booking.objects.create(movie=Movie.objects.get(title="Movie1"),seat=Seat.objects.get(seat_number=12), 
                user=User.objects.get(username="test"))
        