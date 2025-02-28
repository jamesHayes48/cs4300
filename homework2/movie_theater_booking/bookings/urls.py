from django.urls import path, include 
from django.shortcuts import render
from rest_framework.routers import DefaultRouter
from . import views
from .views import MovieViewSet, SeatViewSet, BookingViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet, basename='booking')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.movie_list, name='movie_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('seat_booking/<int:movie_id>/', views.book_seat, name="book_seat"),
    path('booking_history/', views.booking_history, name='booking_history'),
]