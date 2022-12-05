from django.contrib.auth.models import User
from django.db import models
from .validators import validate_postal_code


# Models
class Cinema(models.Model):
    city = models.CharField(max_length=16, unique=True)
    street = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=6, validators=[validate_postal_code])
    email = models.EmailField(max_length=64)
    telephone = models.IntegerField()


class Hall(models.Model):
    nr = models.IntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    seats_columns = models.IntegerField(default=16)
    seats_rows = models.IntegerField(default=12)


class Seat(models.Model):
    nr = models.IntegerField()
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Movie(models.Model):
    title = models.CharField(max_length=64, unique=True)
    year = models.IntegerField()
    description = models.TextField(default=None)


class Genre(models.Model):
    name = models.CharField(max_length=16)
    movie_id = models.ManyToManyField(Movie)


class Screening(models.Model):
    date = models.DateField()
    duration_min = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Reservation(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


class Ticket:
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, unique=True)
