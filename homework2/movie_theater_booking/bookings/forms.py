from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import datetime
from django.utils.timezone import now
from .models import Booking, Seat

class BookingForm(forms.ModelForm):
    # Enforce, that the only seat that can be taken are seats that are not booked
    seat = forms.ModelChoiceField(queryset=Seat.objects.filter(booking_status=False), 
                                  label="Seat Number", empty_label="Select a seat", required=True)
    
    # Enforce that dates cannot be entered before the current day and dates can be up to 90 days in advance
    date = forms.DateField(widget=forms.SelectDateWidget(), 
        validators=[MinValueValidator(datetime.date.today()), MaxValueValidator(datetime.date.today() + datetime.timedelta(days=90))], 
        label="Date", initial=now)
    
    class Meta:
        model = Booking
        fields = ['date', 'seat']

    # Generated by Claude (Anthropic)
    def clean_seat(self):
        selected_seat = self.cleaned_data['seat']
        if selected_seat.booking_status:
            raise ValidationError("This seat is already booked")
        return selected_seat
