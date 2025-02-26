from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404, render
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
    
    @action(detail=False, methods=['get'])
    def available(self, request):
        # Get available seats (where booking_status is False)
        available_seats = Seat.objects.filter(booking_status=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # Return only bookings belonging to the user
    def queryset(self):
        return Booking.objects.filter(user=self.request.user)

    # Override create method in DRF
    def create(self, request, *args, **kwargs):
        seat_id = request.data.get('seat')

        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.booking_status:
                return Response({"error": "This seat is already booked."}, status=status.HTTP_400_BAD_REQUEST)
        
        except Seat.DoesNotExist:
            return Response({"error": "Seat was not found."}, status=status.HTTP_404_NOT_FOUND)

        # Set current user as the booking user
        request.data['user'] = request.user.id

        serializer = BookingSerializer(data=request.data)

        seat.booking_status = True
        seat.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def booking_history(self, request):
        user_bookings = self.get_queryset()
        serializer = BookingSerializer(user_bookings, many=True)
        return Response(serializer.data)


# Return movie_list page
def movie_list(request): 
    # Get all movies from the database
    movies = Movie.objects.all()
    
    # Render the template with the movies context
    return render(request, 'bookings/movie_list.html', {'movies': movies})