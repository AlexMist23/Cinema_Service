from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View, generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

import datetime

from .forms import CinemaForm, HallForm, MovieForm, GenreForm, ScreeningForm, SelectCinemaForm
from .models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation, Ticket


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CinemaAddView(View):
    def get(self, request):
        form = CinemaForm()
        return render(request, 'form/cinema_form.html', {'form': form})

    def post(self, request):
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cinema')
        cnx = {
            "form": form,
        }
        return render(request, 'form/cinema_form.html', cnx)


class CinemaDetailsView(View):
    def get(self, request, cinema_id):
        cinema = Cinema.objects.get(pk=cinema_id)
        halls = Hall.objects.filter(cinema_id=cinema).order_by('nr')
        cnx = {
            'cinema': cinema,
            'halls': halls,
            }
        return render(request, "cinema_details.html", cnx)


class CinemaListView(View):
    def get(self, request):
        cinemas = Cinema.objects.all()
        cnx = {"cinemas": cinemas}
        return render(request, "cinema_list.html", cnx)


class HallAddView(View):
    def get(self, request, cinema_id):
        cinema = Cinema.objects.get(pk=cinema_id)
        form = HallForm(initial={'cinema_id': cinema,
                                 'nr': cinema.hall_set.count() + 1})
        cnx = {
            'cinema': cinema,
            'form': form,
               }
        return render(request, 'form/hall_form.html', cnx)

    def post(self, request, cinema_id):
        form = HallForm(request.POST)
        cinema = Cinema.objects.get(pk=cinema_id)

        if form.is_valid():
            new_hall = form.save()

            for seat_nr in range(new_hall.seats_columns * new_hall.seats_rows):
                s = Seat(nr=seat_nr + 1, hall_id=new_hall)
                s.save()

            return HttpResponseRedirect(f'/cinema/{cinema_id}')
        cnx = {
            'cinema': cinema,
            'form': form,
            }
        return render(request, 'form/hall_form.html', cnx)


class HallDetailsView(View):
    def get(self, request, hall_id):

        hall = Hall.objects.get(pk=hall_id)
        cinema = hall.cinema_id
        seats = hall.seat_set.all()

        cnx = {
            'cinema': cinema,
            'hall': hall,
            'seats': seats,
            }
        return render(request, "hall_details.html", cnx)


class SeatDetailsView(View):
    def get(self, request, seat_id):
        seat = Seat.objects.get(pk=seat_id)
        hall = seat.hall_id
        cinema = hall.cinema_id

        cnx = {
            "seat": seat,
            "hall": hall,
            "cinema": cinema
        }
        return render(request, "seat_details.html", cnx)


class MovieAddView(View):
    def get(self, request):
        form = MovieForm()
        return render(request, 'form/cinema_form.html', {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return HttpResponseRedirect(f'/movie/{movie.id}')
        cnx = {
            "form": form,
        }
        return render(request, 'form/movie_form.html', cnx)


class MovieDetailsView(View):
    def get(self, request, movie_id):
        movie = Movie.objects.get(pk=movie_id)
        genres = movie.genre.all()
        screenings = Screening.objects.filter(movie_id=movie)
        cnx = {
            'movie': movie,
            "genres": genres,
            'screenings': screenings,
        }
        return render(request, "movie_details.html", cnx)


class MovieListView(View):
    def get(self, request):
        movies = Movie.objects.all()
        cnx = {
            "movies": movies,
        }
        return render(request, "movie_list.html", cnx)


class GenreAddView(View):
    def get(self, request):
        form = GenreForm()
        return render(request, 'form/genre_form.html', {'form': form})

    def post(self, request):
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/genre')
        cnx = {
            "form": form,
        }
        return render(request, 'form/genre_form.html', cnx)


class GenreListView(View):
    def get(self, request):
        genres = Genre.objects.all()
        cnx = {"genres": genres}
        return render(request, "genre_list.html", cnx)


class ScreeningAddView(View):
    def get(self, request):
        form = ScreeningForm()
        return render(request, 'form/screening_form.html', {'form': form})

    def post(self, request):
        form = ScreeningForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/screening')
        cnx = {
            "form": form,
        }
        return render(request, 'form/screening_form.html', cnx)


class ScreeningView(View):
    def get(self, request):
        screenings = Screening.objects.all()
        cnx = {
            "screenings": screenings
        }
        return render(request, 'screenings.html', cnx)


class LandingPageView(View):
    def get(self, request):
        select_cinema = SelectCinemaForm()
        return render(request, 'landing_page.html', {'select_cinema': select_cinema})


class RepertuarView(View):
    def get(self, request):
        date = datetime.date.today()
        screenings = Screening.objects.filter(date=date)
        cnx = {
            "screenings": screenings
        }
        return render(request, 'repertuar.html', cnx)
