from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
from django.urls import reverse, resolve

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
        data = {"title": "Movie1",
            "description": "Movie 1 moment",
            "release_date": "2024-03-01",
            "duration": 301}
        url = reverse('movies-list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test if anonymous users can create new movies
    def test_movie_creation_anonymous(self):
        self.client.logout()
        data = {"title": "Movie1",
            "description": "Movie 1 moment",
            "release_date": "2024-03-01",
            "duration": 301}
        url = reverse('movies-list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # Test if admins can create new movies
    def test_movie_creation_admin(self):
        self.client.force_authenticate(user=self.admin)
        data = {"title": "Movie1",
            "description": "Movie 1 moment",
            "release_date": "2024-03-01",
            "duration": 301}
        url = reverse('movies-list')
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class SeatViewTestCase(APITestCase):
    def setUp(self):
        self.reg_user = User.objects.create_user(username="test", password="test")
        self.admin = User.objects.create_superuser(username="admin", password="test")