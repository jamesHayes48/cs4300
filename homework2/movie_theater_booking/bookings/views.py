from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import(IsAuthenticated, IsAdminUser, )

# Create your views here.
class MovieViewSet(viewsets.ViewSet):
    """
    ViewSet for CRUD Operations for movies
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    

class SeatViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving seats.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def queryset(self):
        return Booking.objects.filter(user=self.request.user)