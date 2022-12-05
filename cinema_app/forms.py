from django.forms import ModelForm
from .models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation, Ticket
from django import forms
from .validators import validate_postal_code


class CinemaForm(ModelForm):
    postal_code = forms.CharField(max_length=6, validators=[validate_postal_code], required=True)

    class Meta:
        model = Cinema
        fields = ['city', 'street', 'postal_code', 'email', 'telephone']


class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'


class Form(ModelForm):
    class SeatMeta:
        model = Seat
        fields = '__all__'


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
