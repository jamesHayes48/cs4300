from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404, render
from rest_framework import permissions
from rest_framework.permissions import(IsAuthenticated, IsAdminUser, )
from .forms import BookingForm

# Generated by Claude (Anthropic)
class MovieViewSet(viewsets.ModelViewSet):
    """
    ViewSet for CRUD Operations for movies, only admins can handle this model
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    '''
    Allow Users to list or retrieve movies
    Allow Admins to create movies
    '''
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


# Generated by Claude (Anthropic)
class SeatViewSet(viewsets.ModelViewSet):
    """
    ViewSet for listing and retrieving seats.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    
    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'available':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def available(self, request):
        # Get available seats (where booking_status is False)
        available_seats = Seat.objects.filter(booking_status=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)

    

# Generated by Claude (Anthropic)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

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

        if serializer.is_valid():
            booking = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def booking_history(self, request):
        user_bookings = Booking.objects.filter(user=self.request.user)
        serializer = BookingSerializer(user_bookings, many=True)
        return Response(serializer.data)


# Return movie_list page
def movie_list(request): 
    # Get all movies from the database
    movies = MovieViewSet.queryset
    
    # Render the template with the movies context
    return render(request, 'bookings/movie_list.html', {'movies': movies})

# Generated by Claude (Anthropic)
# Display user form request for booking a seat
@login_required
def book_seat(request, movie_id):
    context = {}
    selected_movie = get_object_or_404(Movie, id=movie_id)
    form = BookingForm()

    # Scan for post request
    if request.method == 'POST':
        form = BookingForm(request.POST)

        # If it is valid, pull in data from user request and save the seat object's status
        if form.is_valid():
            selected_seat = form.cleaned_data['seat']
            selected_date = form.cleaned_data['date']

            booking = Booking.objects.create(movie=selected_movie, seat=selected_seat, booking_date=selected_date, user=request.user)
            selected_seat.booking_status = True
            selected_seat.save()

    context['form'] = form
    context['movie'] = selected_movie
          
    return render(request, 'bookings/seat_booking.html', context)

# Return user's bookings made
@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)

    return render(request, 'bookings/booking_history.html', {'bookings': bookings})