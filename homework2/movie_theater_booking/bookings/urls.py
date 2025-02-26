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
    path('', include(router.urls)),

    path('movie_list/', views.movie_list, name='movie_list'),
    #path('booking_history/', views.booking_history, name='booking_history'),
    #path('seat_booking/', views.seat_booking, name='seat_booking'),
]