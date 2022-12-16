"""Cinema_Service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from cinema_app.views import LandingPageView, SignUpView, CinemaAddView, CinemaDetailsView, CinemaListView,\
    HallAddView, HallDetailsView, SeatDetailsView, MovieAddView, MovieListView, MovieDetailsView,\
    GenreListView, GenreAddView, ScreeningListView, ScreeningAddView, ScreeningDetailsView, RepertuarView,\
    ReservationAddView, ReservationsListView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cinema/', CinemaListView.as_view(), name='cinema_list'),
    path('cinema/add/', CinemaAddView.as_view(), name='cinema_add'),
    path('cinema/<int:cinema_id>/', CinemaDetailsView.as_view(), name='cinema_details'),
    path('cinema/<int:cinema_id>/add_hall/', HallAddView.as_view(), name='hall_add'),
    path('hall/<int:hall_id>/', HallDetailsView.as_view(), name='hall_details'),
    path('seat/<int:seat_id>/', SeatDetailsView.as_view(), name='seat_details'),
    path('movie/', MovieListView.as_view(), name='movie_list'),
    path('movie/add/', MovieAddView.as_view(), name='movie_add'),
    path('movie/<int:movie_id>/', MovieDetailsView.as_view(), name='movie_details'),
    path('genre/', GenreListView.as_view(), name='genre_list'),
    path('genre/add/', GenreAddView.as_view(), name='movie_list'),
    path('screening/', ScreeningListView.as_view(), name='screening_list'),
    path('screening/add/', ScreeningAddView.as_view(), name='screening_add'),
    path('screening/<int:screening_id>/', ScreeningDetailsView.as_view(), name='screening_details'),
    re_path(r'^screening/(?P<screening_id>\d+)/(?P<seats>(\d{1,4},)+)/$',
            ReservationAddView.as_view(), name='reservation_add'),
    path('repertuar/', LandingPageView.as_view(), name='home'),
    path('repertuar/<str:cinema_name>/', RepertuarView.as_view(), name='repertuar'),
    path('reservations/', ReservationsListView.as_view(), name='reservation'),
    path('', LandingPageView.as_view(), name='landing_page'),
]
