from django import forms
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
import datetime
from .models import Booking, Seat

class BookingForm(forms.ModelForm):
    # Enforce, that the only seat that can be taken are seats that are not booked
    seat = forms.ModelChoiceField(queryset=Seat.objects.filter(booking_status=False), 
                                  label="Seat Number", empty_label="Select a seat", required=True)
    
    # Enforce that dates cannot be entered before the current day
    date = forms.DateField(widget=forms.SelectDateWidget(), validators=[MinValueValidator(datetime.date.today())], label="Booking Date")
    class Meta:
        model = Booking
        fields = ['date', 'seat']
    
    def clean_seat(self):
        selected_seat = self.cleaned_data['seat']
        if selected_seat.booking_status:
            raise ValidationError("This seat is already booked")
        return selected_seat