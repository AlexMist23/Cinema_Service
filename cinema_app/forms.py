from django import forms
from django.forms import ModelForm
from django.forms.widgets import SplitDateTimeWidget
from django.core.exceptions import ObjectDoesNotExist

from .models import Cinema, Hall, Movie, Genre, Screening, Reservation


class CinemaForm(ModelForm):
    """Form for creating object of model Cinema"""
    class Meta:
        model = Cinema
        fields = '__all__'


class HallForm(ModelForm):
    """Form for creating object of model Hall"""
    class Meta:
        model = Hall
        fields = '__all__'


class MovieForm(ModelForm):
    """Form for creating object of model Movie"""
    class Meta:
        model = Movie
        fields = '__all__'


class GenreForm(ModelForm):
    """Form for creating object of model Genre"""
    class Meta:
        model = Genre
        fields = '__all__'


class ScreeningForm(ModelForm):
    """Form for creating object of model Screening"""
    start_date = forms.SplitDateTimeField(widget=SplitDateTimeWidget(), help_text='MM/DD/YYYY, HH:MM')
    end_date = forms.SplitDateTimeField(widget=SplitDateTimeWidget(), help_text='MM/DD/YYYY, HH:MM')

    class Meta:
        model = Screening
        fields = ['start_date', 'end_date', 'movie_id', 'hall_id']


class SelectCinemaForm(forms.Form):
    """
    Form for creating list of the Cinemas to choose
    Catching Error when there is no Cinema model objects in Database
    """
    try:
        all_cinemas = Cinema.objects.all()
    except ObjectDoesNotExist:
        pass

    select_cinema = forms.ModelChoiceField(queryset=all_cinemas,
                                           initial=all_cinemas.order_by('id')[0])


class ReservationForm(ModelForm):
    """Form for creating object of model Reservation"""
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['seat_id', 'available']
        widgets = {
            'screening_id': forms.HiddenInput,
            'user_id': forms.HiddenInput
            }
