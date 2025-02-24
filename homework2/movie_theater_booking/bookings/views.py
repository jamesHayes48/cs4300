from .models import Movie, Seat, Booking
from .serializers import MovieSerializer
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

    def list(self, request):
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        pass
    
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    def create(self, request):
        pass


class SeatViewSet(viewsets.ViewSet):
    """
    ViewSet for listing and retrieving seats.
    """

    def create(self, request):
        pass
    
    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

    def create(self, request):
        pass

