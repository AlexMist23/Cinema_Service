from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
import pytest

from cinema_app.views import LandingPageView, SignUpView, CinemaAddView, CinemaDetailsView, CinemaListView,\
    HallAddView, HallDetailsView, SeatDetailsView, MovieAddView, MovieListView, MovieDetailsView,\
    GenreListView, GenreAddView, ScreeningListView, ScreeningAddView, ScreeningDetailsView, RepertuarView,\
    ReservationAddView, ReservationsListView

from cinema_app.models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation


class TestUrl(SimpleTestCase):
    """Test if url connects to proper View"""

    def test_sign_up(self):
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, SignUpView)

    def test_cinema_list(self):
        url = reverse('cinema_list')
        self.assertEquals(resolve(url).func.view_class, CinemaListView)

    def test_cinema_add(self):
        url = reverse('cinema_add')
        self.assertEquals(resolve(url).func.view_class, CinemaAddView)

    def test_cinema_details(self):
        url = reverse('cinema_details', kwargs={'cinema_id': 1})
        self.assertEquals(resolve(url).func.view_class, CinemaDetailsView)

    def test_hall_add(self):
        url = reverse('hall_add', kwargs={'cinema_id': 1})
        self.assertEquals(resolve(url).func.view_class, HallAddView)

    def test_hall_details(self):
        url = reverse('hall_details', kwargs={'hall_id': 1})
        self.assertEquals(resolve(url).func.view_class, HallDetailsView)

    def test_seat_details(self):
        url = reverse('seat_details', kwargs={'seat_id': 1})
        self.assertEquals(resolve(url).func.view_class, SeatDetailsView)

    def test_movie_list(self):
        url = reverse('movie_list')
        self.assertEquals(resolve(url).func.view_class, MovieListView)

    def test_movie_add(self):
        url = reverse('movie_add')
        self.assertEquals(resolve(url).func.view_class, MovieAddView)

    def test_movie_details(self):
        url = reverse('movie_details', kwargs={'movie_id': 1})
        self.assertEquals(resolve(url).func.view_class, MovieDetailsView)

    def test_genre_list(self):
        url = reverse('genre_list')
        self.assertEquals(resolve(url).func.view_class, GenreListView)

    def test_genre_add(self):
        url = reverse('genre_add')
        self.assertEquals(resolve(url).func.view_class, GenreAddView)

    def test_screening_list(self):
        url = reverse('screening_list')
        self.assertEquals(resolve(url).func.view_class, ScreeningListView)

    def test_screening_add(self):
        url = reverse('screening_add')
        self.assertEquals(resolve(url).func.view_class, ScreeningAddView)

    def test_screening_details(self):
        url = reverse('screening_details', kwargs={'screening_id': 1})
        self.assertEquals(resolve(url).func.view_class, ScreeningDetailsView)

    def test_reservation_add(self):
        url = reverse('reservation_add', kwargs={'screening_id': 1, 'seats': '1,'})
        self.assertEquals(resolve(url).func.view_class, ReservationAddView)

    def test_cinema_select(self):
        url = reverse('cinema_select')
        self.assertEquals(resolve(url).func.view_class, LandingPageView)

    def test_repertuar(self):
        url = reverse('repertuar_cinema', kwargs={'cinema_name': 'city'})
        self.assertEquals(resolve(url).func.view_class, RepertuarView)

    def test_reservations(self):
        url = reverse('reservations')
        self.assertEquals(resolve(url).func.view_class, ReservationsListView)

    def test_landing_page(self):
        url = reverse('landing_page')
        self.assertEquals(resolve(url).func.view_class, LandingPageView)
