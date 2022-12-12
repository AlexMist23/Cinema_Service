from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from .validators import postal_code_validation


# Models
class Cinema(models.Model):
    city = models.CharField(max_length=16, unique=True)
    street = models.CharField(max_length=32)
    postal_code = models.CharField(max_length=6, validators=[postal_code_validation])
    email = models.EmailField(max_length=64)
    telephone = models.CharField(max_length=9, validators=[RegexValidator(r'\d{9}', 'number must have 9 digits')])

    def __str__(self):
        return f'Cinema: {self.city}'


class Hall(models.Model):
    nr = models.PositiveIntegerField()
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    seats_columns = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5),
                                                                            MaxValueValidator(25)])
    seats_rows = models.PositiveSmallIntegerField(default=5, validators=[MinValueValidator(5),
                                                                         MaxValueValidator(25)])

    class Meta:
        unique_together = ('nr', 'cinema_id')

    def __str__(self):
        return f'{self.cinema_id}, Hall nr {self.nr}'


class Seat(models.Model):
    nr = models.PositiveIntegerField()
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nr', 'hall_id')


class Genre(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f'Genre: {self.name}'


class Movie(models.Model):
    title = models.CharField(max_length=64, unique=True)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1900)])
    description = models.TextField(default=None)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return f'Movie: {self.title}'


class Screening(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)


class Reservation(models.Model):
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


class Ticket(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    Reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, unique=True)