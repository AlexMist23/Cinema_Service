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
from django.urls import path, include

from cinema_app.views import LandingPageView, SignUpView, \
    CinemaAddView, CinemaDetailsView, CinemaListView, \
    HallAddView, HallDetailsView, \
    SeatDetailsView, \
    MovieAddView, MovieListView, MovieDetailsView, \
    GenreListView, GenreAddView, \
    ScreeningView, ScreeningAddView, \
    RepertuarView


urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('cinema/', CinemaListView.as_view()),
    path('cinema/add/', CinemaAddView.as_view()),
    path('cinema/<int:cinema_id>/', CinemaDetailsView.as_view()),
    path('cinema/<int:cinema_id>/add_hall/', HallAddView.as_view()),
    path('hall/<int:hall_id>', HallDetailsView.as_view()),
    path('seat/<int:seat_id>', SeatDetailsView.as_view()),
    path('movie/', MovieListView.as_view()),
    path('movie/add/', MovieAddView.as_view()),
    path('movie/<int:movie_id>/', MovieDetailsView.as_view()),
    path('genre/', GenreListView.as_view()),
    path('genre/add/', GenreAddView.as_view()),
    path('screening/', ScreeningView.as_view()),
    path('screening/add/', ScreeningAddView.as_view()),
    path('repertuar/', LandingPageView.as_view()),
    path('', LandingPageView.as_view()),
]
