from django import forms
from .models import Car, Rental

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'release_year', 'rental_price_per_day', 'capacity', 'transmission', 'added_by', 'phone_number', 'city', 'photo1', 'photo2', 'photo3']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['start_date', 'end_date']