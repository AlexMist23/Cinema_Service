from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from datetime import datetime, timedelta, time

from .forms import CinemaForm, HallForm, MovieForm, GenreForm, ScreeningForm, SelectCinemaForm, ReservationForm
from .models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CinemaAddView(LoginRequiredMixin, View):
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
        cinema = get_object_or_404(Cinema, pk=cinema_id)
        halls = Hall.objects.filter(cinema_id=cinema).order_by('nr')
        cnx = {
            'cinema': cinema,
            'halls': halls,
        }
        return render(request, "cinema_details.html", cnx)


class CinemaListView(LoginRequiredMixin, View):
    def get(self, request):
        cinemas = Cinema.objects.all()
        cnx = {"cinemas": cinemas}
        return render(request, "cinema_list.html", cnx)


class HallAddView(LoginRequiredMixin, View):
    def get(self, request, cinema_id):
        cinema = get_object_or_404(Cinema, pk=cinema_id)
        form = HallForm(initial={'cinema_id': cinema,
                                 'nr': cinema.hall_set.count() + 1})
        cnx = {
            'cinema': cinema,
            'form': form,
        }
        return render(request, 'form/hall_form.html', cnx)

    def post(self, request, cinema_id):
        form = HallForm(request.POST)
        cinema = get_object_or_404(Cinema, pk=cinema_id)

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


class HallDetailsView(LoginRequiredMixin, View):
    def get(self, request, hall_id):
        hall = get_object_or_404(Hall, pk=hall_id)
        cinema = hall.cinema_id
        seats = hall.seat_set.all()

        cnx = {
            'cinema': cinema,
            'hall': hall,
            'seats': seats,
        }
        return render(request, "hall_details.html", cnx)


class SeatDetailsView(LoginRequiredMixin, View):
    def get(self, request, seat_id):
        seat = get_object_or_404(Seat, pk=seat_id)
        hall = seat.hall_id
        cinema = hall.cinema_id

        cnx = {
            "seat": seat,
            "hall": hall,
            "cinema": cinema
        }
        return render(request, "seat_details.html", cnx)


class MovieAddView(LoginRequiredMixin, View):
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
        movie = get_object_or_404(Movie, pk=movie_id)
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


class GenreAddView(LoginRequiredMixin, View):
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


class ScreeningAddView(LoginRequiredMixin, View):
    def get(self, request):
        form = ScreeningForm()
        return render(request, 'form/screening_form.html', {'form': form})

    def post(self, request):
        form = ScreeningForm(request.POST)
        if form.is_valid():
            new_screening = form.save()
            hall = new_screening.hall_id
            seats = hall.seat_set.all()
            for seat in seats:
                new_reservation = Reservation(seat_id=seat, screening_id=new_screening)
                new_reservation.save()
            return HttpResponseRedirect('/screening')
        cnx = {
            "form": form,
        }
        return render(request, 'form/screening_form.html', cnx)


class ScreeningListView(View):
    def get(self, request):
        screenings = Screening.objects.all()
        cnx = {
            "screenings": screenings
        }
        return render(request, 'screenings.html', cnx)


class ScreeningDetailsView(View):
    def get(self, request, screening_id):
        screening = get_object_or_404(Screening, pk=screening_id)
        hall = screening.hall_id
        cinema = hall.cinema_id
        seats = hall.seat_set.all().order_by('nr')
        movie = screening.movie_id
        reservations_nums = [reservation.seat_id.nr for reservation in
                             screening.reservation_set.all()]

        cnx = {
            'movie': movie,
            'screening': screening,
            'cinema': cinema,
            'hall': hall,
            'seats': seats,
            'reservations_nums': reservations_nums
        }
        return render(request, "screening_details.html", cnx)


class LandingPageView(View):
    def get(self, request):
        select_cinema = SelectCinemaForm()
        return render(request, 'landing_page.html', {'select_cinema': select_cinema})

    def post(self, request):
        select_cinema = SelectCinemaForm(request.POST)
        if select_cinema.is_valid():
            cinema_name = select_cinema.cleaned_data['select_cinema'].city
            return HttpResponseRedirect(f'/repertuar/{cinema_name}')
        cnx = {
            "select_cinema": select_cinema,
        }
        return render(request, 'form/screening_form.html', cnx)


class RepertuarView(View):
    def get(self, request, cinema_name):
        cinema = get_object_or_404(Cinema, city=cinema_name)
        halls = Hall.objects.filter(cinema_id=cinema)
        screenings = Screening.objects.filter(hall_id__in=halls)
        repertuar_days = []
        screenings_per_day = []
        movies_per_day = []
        days = []

        def screening_of_day(result_date):  # result_date = datetime.now().date() + timedelta(n)
            today = result_date
            tomorrow = today + timedelta(1)
            today_start = datetime.combine(today, time())
            today_end = datetime.combine(tomorrow, time())
            return screenings.filter(start_date__lte=today_end, start_date__gt=today_start)

        for day in range(7):
            repertuar_days.append([])
            screenings_per_day.append(screening_of_day(datetime.now().date() + timedelta(day)))
            days.append(datetime.now().date() + timedelta(day))
            repertuar_days[day].append(days[day])
            repertuar_days[day].append(screenings_per_day[day])
        cnx = {
            "screenings_per_day": screenings_per_day,
            "movies_per_day": movies_per_day,
            "days": days,
            "repertuar_days": repertuar_days,
        }
        return render(request, 'repertuar.html', cnx)


class ReservationAddView(LoginRequiredMixin, View):
    def get(self, request, screening_id, seats):
        screening = get_object_or_404(Screening, pk=screening_id)
        seats_nums = seats[:-1].split(',')  # Taking seats numbers into array
        hall = screening.hall_id
        cinema = hall.cinema_id
        user = request.user

        form = ReservationForm(initial={'screening_id': screening,
                                        'user_id': user})
        cnx = {
            'cinema': cinema,
            'hall': hall,
            'screening': screening,
            'seats': seats_nums,
            'form': form,
            'user': user
        }
        return render(request, 'form/reservation_form.html', cnx)

    def post(self, request, screening_id, seats):

        screening = get_object_or_404(Screening, pk=screening_id)
        seats_nums = seats[:-1].split(',')  # Taking seats numbers into array
        hall = screening.hall_id
        cinema = hall.cinema_id
        user = request.user

        form = ReservationForm(request.POST)
        if form.is_valid():
            screening_id = form.cleaned_data['screening_id']
            user_id = form.cleaned_data['user_id']

            for seat_nr in seats_nums:
                seat = get_object_or_404(Seat, nr=seat_nr, hall_id=hall)
                reservation = Reservation(screening_id=screening_id, seat_id=seat, user_id=user_id)
                reservation.save()

            return HttpResponseRedirect(f'/reservations')
        cnx = {
            'cinema': cinema,
            'hall': hall,
            'screening': screening,
            'seats': seats_nums,
            'form': form,
            'user': user
        }
        return render(request, 'form/screening_form.html', cnx)


class ReservationsListView(LoginRequiredMixin, View):
    def get(self, request):
        reservations = Reservation.objects.filter(user_id=request.user)
        cnx = {
            "reservations": reservations
        }
        return render(request, 'user_reservations.html', cnx)
