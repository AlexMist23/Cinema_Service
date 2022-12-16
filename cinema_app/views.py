from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View, generic
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404

from .forms import CinemaForm, HallForm, MovieForm, GenreForm, ScreeningForm, SelectCinemaForm, ReservationForm
from .models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CinemaAddView(View):
    @staticmethod
    def get(request):
        form = CinemaForm()
        return render(request, 'form/cinema_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = CinemaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cinema')
        cnx = {
            "form": form,
        }
        return render(request, 'form/cinema_form.html', cnx)


class CinemaDetailsView(View):
    @staticmethod
    def get(request, cinema_id):
        cinema = get_object_or_404(Cinema, pk=cinema_id)
        halls = Hall.objects.filter(cinema_id=cinema).order_by('nr')
        cnx = {
            'cinema': cinema,
            'halls': halls,
            }
        return render(request, "cinema_details.html", cnx)


class CinemaListView(View):
    @staticmethod
    def get(request):
        cinemas = get_list_or_404(Cinema)
        cnx = {"cinemas": cinemas}
        return render(request, "cinema_list.html", cnx)


class HallAddView(View):
    @staticmethod
    def get(request, cinema_id):
        cinema = get_object_or_404(Cinema, pk=cinema_id)
        form = HallForm(initial={'cinema_id': cinema,
                                 'nr': cinema.hall_set.count() + 1})
        cnx = {
            'cinema': cinema,
            'form': form,
               }
        return render(request, 'form/hall_form.html', cnx)

    @staticmethod
    def post(request, cinema_id):
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


class HallDetailsView(View):
    @staticmethod
    def get(request, hall_id):

        hall = get_object_or_404(Hall, pk=hall_id)
        cinema = hall.cinema_id
        seats = hall.seat_set.all()

        cnx = {
            'cinema': cinema,
            'hall': hall,
            'seats': seats,
            }
        return render(request, "hall_details.html", cnx)


class SeatDetailsView(View):
    @staticmethod
    def get(request, seat_id):
        seat = get_object_or_404(Seat, pk=seat_id)
        hall = seat.hall_id
        cinema = hall.cinema_id

        cnx = {
            "seat": seat,
            "hall": hall,
            "cinema": cinema
        }
        return render(request, "seat_details.html", cnx)


class MovieAddView(View):
    @staticmethod
    def get(request):
        form = MovieForm()
        return render(request, 'form/cinema_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return HttpResponseRedirect(f'/movie/{movie.id}')
        cnx = {
            "form": form,
        }
        return render(request, 'form/movie_form.html', cnx)


class MovieDetailsView(View):
    @staticmethod
    def get(request, movie_id):
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
    @staticmethod
    def get(request):
        movies = Movie.objects.all()
        cnx = {
            "movies": movies,
        }
        return render(request, "movie_list.html", cnx)


class GenreAddView(View):
    @staticmethod
    def get(request):
        form = GenreForm()
        return render(request, 'form/genre_form.html', {'form': form})

    @staticmethod
    def post(request):
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/genre')
        cnx = {
            "form": form,
        }
        return render(request, 'form/genre_form.html', cnx)


class GenreListView(View):
    @staticmethod
    def get(request):
        genres = get_list_or_404(Genre)
        cnx = {"genres": genres}
        return render(request, "genre_list.html", cnx)


class ScreeningAddView(View):
    @staticmethod
    def get(request):
        form = ScreeningForm()
        return render(request, 'form/screening_form.html', {'form': form})

    @staticmethod
    def post(request):
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
    @staticmethod
    def get(request):
        screenings = get_list_or_404(Screening)
        cnx = {
            "screenings": screenings
        }
        return render(request, 'screenings.html', cnx)


class ScreeningDetailsView(View):
    @staticmethod
    def get(request, screening_id):
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
    @staticmethod
    def get(request):
        select_cinema = SelectCinemaForm()
        return render(request, 'landing_page.html', {'select_cinema': select_cinema})

    @staticmethod
    def post(request):
        select_cinema = SelectCinemaForm(request.POST)
        if select_cinema.is_valid():
            cinema_name = select_cinema.cleaned_data['select_cinema'].city
            return HttpResponseRedirect(f'/repertuar/{cinema_name}')
        cnx = {
            "select_cinema": select_cinema,
        }
        return render(request, 'form/screening_form.html', cnx)


class RepertuarView(View):
    @staticmethod
    def get(request, cinema_name):
        cinema = get_object_or_404(Cinema, city=cinema_name)
        halls = Hall.objects.filter(cinema_id=cinema)
        screenings = Screening.objects.filter(hall_id__in=halls)
        cnx = {
            "screenings": screenings
        }
        return render(request, 'repertuar.html', cnx)


class ReservationAddView(View):
    @staticmethod
    def get(request, screening_id, seats):
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

    @staticmethod
    def post(request, screening_id, seats):

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


class ReservationsListView(View):
    @staticmethod
    def get(request):
        reservations = Reservation.objects.filter(user_id=request.user)
        cnx = {
            "reservations": reservations
        }
        return render(request, 'user_reservations.html', cnx)
