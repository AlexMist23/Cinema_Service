from django.forms import ModelForm
from .models import Cinema, Hall, Movie, Genre, Screening, Reservation, Ticket


class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        fields = '__all__'


class HallForm(ModelForm):
    class Meta:
        model = Hall
        fields = '__all__'


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'
