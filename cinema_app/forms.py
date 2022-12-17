from django import forms
from django.forms import ModelForm
from django.forms.widgets import SplitDateTimeWidget
from django.core.exceptions import ObjectDoesNotExist

from .models import Cinema, Hall, Movie, Genre, Screening, Reservation


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


class ScreeningForm(ModelForm):
    start_date = forms.SplitDateTimeField(widget=SplitDateTimeWidget(), help_text='MM/DD/YYYY, HH:MM')
    end_date = forms.SplitDateTimeField(widget=SplitDateTimeWidget(), help_text='MM/DD/YYYY, HH:MM')

    class Meta:
        model = Screening
        fields = ['start_date', 'end_date', 'movie_id', 'hall_id']


class SelectCinemaForm(forms.Form):
    try:
        all_cinemas = Cinema.objects.all()
    except ObjectDoesNotExist:
        pass

    select_cinema = forms.ModelChoiceField(queryset=all_cinemas,
                                           initial=all_cinemas.order_by('id')[0])

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        exclude = ['seat_id', 'available']
        widgets = {
            'screening_id': forms.HiddenInput,
            'user_id': forms.HiddenInput
            }
