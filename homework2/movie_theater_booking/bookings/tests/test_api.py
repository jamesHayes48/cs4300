from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
from bookings.serializers import BookingSerializer
from django.urls import reverse, resolve
import datetime
from django.utils.timezone import now

'''
Test the API for movies with authenticated, anonymous, and admin users
'''
class MovieViewTestCase(APITestCase):
    def setUp(self):
        self.reg_user = User.objects.create_user(username="test", password="test")
        self.admin = User.objects.create_superuser(username="admin", password="test")


    # Test if regular users can get movies
    def test_movie_listing_reg_user(self):
        self.client.force_authenticate(user=self.reg_user)
        url = reverse('movies-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test if unauthenticated users can see movie list
    def test_movie_listing_anonymous(self):
        self.client.logout()
        url = reverse('movies-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test if admin can see movie list
    def test_movie_listing_admin(self):
        self.client.force_authenticate(user=self.admin)
        url = reverse('movies-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test if regular users can create a new movie (they should not be able to)
    def test_movie_creation_reg_user(self):
        self.client.force_authenticate(user=self.reg_user)
        new_movie = {"title": "Movie1",
            "description": "Movie 1 moment",
            "release_date": "2024-03-01",
            "duration": 301}
        url = reverse('movies-list')
        response = self.client.post(url, new_movie, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test if anonymous users can create new movies
    def test_movie_creation_anonymous(self):
        self.client.logout()
        new_movie = {"title": "Movie1",
            "description": "Movie 1 moment",
            "release_date": "2024-03-01",
            "duration": 301}
        url = reverse('movies-list')
        response = self.client.post(url, new_movie, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test if admins can create new movies
    def test_movie_creation_admin(self):
        self.client.force_authenticate(user=self.admin)
        new_movie = {"title": "Movie1",
            "description": "Movie 1 moment",
            "release_date": "2024-03-01",
            "duration": 301}
        url = reverse('movies-list')
        response = self.client.post(url, new_movie, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

'''
Test the seat API for creation and availability function
'''
class SeatViewTestCase(APITestCase):
    def setUp(self):
        self.reg_user = User.objects.create_user(username="test", password="test")
        self.admin = User.objects.create_superuser(username="admin", password="test")
        self.seat_12 = Seat.objects.create(seat_number=12)
        self.seat_13 = Seat.objects.create(seat_number=13, booking_status=True)

    def test_available(self):
        # Test if client can see the seats
        self.client.logout()
        url = reverse('seats-available')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        available_seats = response.data

        # Test if available seats are correct
        seats_returned = [seat['seat_number'] for seat in available_seats]
        self.assertIn(12, seats_returned)
        self.assertNotIn(13, seats_returned)
    
    def test_seat_creation_reg_user(self):
        self.client.force_authenticate(user=self.reg_user)
        new_seat = {"seat_number": 10, "booking_status": True}
        url = reverse('seats-list')
        response = self.client.post(url, new_seat, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_seat_creation_anonymous(self):
        self.client.logout()
        new_seat = {"seat_number": 10, "booking_status": True}
        url = reverse('seats-list')
        response = self.client.post(url, new_seat, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_seat_creation_admin(self):
        self.client.force_authenticate(user=self.admin)
        new_seat = {"seat_number": 10}
        url = reverse('seats-list')
        response = self.client.post(url, new_seat, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

'''
Test the booking view test case
'''
class BookingViewTestCase(APITestCase):
    def setUp(self):
        self.reg_user = User.objects.create_user(username="test", password="test")
        self.admin = User.objects.create_superuser(username="admin", password="test")
        self.seat_12 = Seat.objects.create(seat_number=12)
        self.seat_13 = Seat.objects.create(seat_number=13, booking_status=True)
        self.Movie_1 = Movie.objects.create(title="Movie 1", 
            description="Blah blah blah", release_date="1950-05-11", duration=12)
    
    # Test creation of booking
    def test_booking_creation(self):
        self.client.force_authenticate(user=self.reg_user)
        valid_booking = {"movie": self.Movie_1.id, "seat": self.seat_12.id, "user": self.reg_user.id, 
            "booking_date": datetime.date.today()}
        url = reverse("booking-list")
        response = self.client.post(url, valid_booking, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test if a booking of the same seat can be made
        self.client.force_authenticate(user=self.admin)
        invalid_booking = {"movie": self.Movie_1.id, "seat": self.seat_12.id, "user": self.admin.id, 
            "booking_date": datetime.date.today()}
        url = reverse("booking-list")
        response = self.client.post(url, valid_booking, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_booking_history(self):
        self.client.force_authenticate(user=self.reg_user)

        # Create a booking, and check if the user matches with the user requesting it
        valid_booking = {"movie": self.Movie_1.id, "seat": self.seat_12.id, "user": self.reg_user.id, 
            "booking_date": datetime.date.today()}
        url = reverse("booking-list")
        response = self.client.post(url, valid_booking, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check for response from booking history
        url = reverse('booking-booking-history')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bookings = response.data

        # Check if the booking is the user's booking
        my_booking = [booking['user'] for booking in bookings]
        self.assertIn(self.reg_user.id, my_booking)