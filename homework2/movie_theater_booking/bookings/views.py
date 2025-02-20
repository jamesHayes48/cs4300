from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.
class MovieViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving movies.
    """

class SeatViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving seats.
    """

class BookingViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving booking history.
    """