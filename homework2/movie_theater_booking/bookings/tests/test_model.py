from django.test import TestCase
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
from datetime import date, timedelta
from django.utils.timezone import now

# Create your tests here.
class MovieTestCase(TestCase):
    def setUp(self):
        Movie.objects.create(title="Movie1", description="xyz",
            release_date=date(2003, 11, 11), duration=120)

    # Test creation of tests
    def test_movie_creation(self):
        movie_1 = Movie.objects.get(title="Movie1")
        self.assertEqual(movie_1.title, "Movie1")
        self.assertEqual(movie_1.description, "xyz")
        self.assertEqual(movie_1.release_date, date(2003, 11, 11))
        self.assertEqual(movie_1.duration, 120)

class SeatTestCase(TestCase):
    def setUp(self):
        self.valid_seat_num = 10
        self.invalid_seat_num = 12

    def test_seat_creation(self):
        seat_10 = Seat.objects.create(seat_number=self.valid_seat_num)
        self.assertEqual(seat_10.seat_number, self.valid_seat_num)
        self.assertEqual(seat_10.booking_status, False)
    
    def test_invalid_seat_creation(self):
        seat_12 = Seat.objects.create(seat_number=self.invalid_seat_num)
        
        with self.assertRaises(ValidationError):
            seat_12.full_clean()    

class BookingTestCase(TestCase):
    def setUp(self):
        self.movie_1 = Movie.objects.create(title="Movie1", description="xyz",
            release_date=date(2003, 11, 11), duration=120)
        self.seat_10 = Seat.objects.create(seat_number=10)
        self.user = User.objects.create_user(username="test", password="test")
        Booking.objects.all().delete()
        

    # Check valid booking creation
    def test_booking_creation(self):
        booking_1 = Booking.objects.create(movie=self.movie_1, seat=self.seat_10, 
            user=self.user, booking_date=date.today())

        # Test booking ties with movie object
        self.assertEqual(booking_1.movie.title, "Movie1")
        self.assertEqual(booking_1.movie.description, "xyz")
        self.assertEqual(booking_1.movie.release_date, date(2003, 11, 11))
        self.assertEqual(booking_1.movie.duration, 120)

        # Test booking ties with seat object
        self.assertEqual(booking_1.seat.seat_number, 10)
        # This setting is set to true for the book_seat function in views.py
        self.assertEqual(booking_1.seat.booking_status, False)

        # Test that another object cannot be created with the unique fields
        with self.assertRaises(IntegrityError):
            Booking.objects.create(movie=self.movie_1, seat=self.seat_10, 
                user=self.user)
        
    # Test if booking can be made before the current date
    def test_booking_creation_before(self):
        booking = Booking.objects.create(movie=self.movie_1, seat=self.seat_10, 
            user=self.user, booking_date= date.today() - timedelta(days=90))

        with self.assertRaises(ValidationError):
            booking.full_clean()

    # Test if booking can be made past 90 days for the booking
    def test_booking_creation_after(self):
        booking = Booking.objects.create(movie=self.movie_1, seat=self.seat_10, 
            user=self.user, booking_date= date.today() + timedelta(days=91))  

        with self.assertRaises(ValidationError): 
            booking.full_clean()