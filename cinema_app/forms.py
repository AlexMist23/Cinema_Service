from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms
from .models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation, Ticket


class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'


class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'
        exclude = ['cinema_id']


class Form(ModelForm):
    class SeatMeta:
        model = Seat
        fields = '__all__'


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
