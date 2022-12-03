from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View, generic
from django.urls import reverse_lazy
from .forms import CinemaForm, HallForm
from .models import Cinema, Hall, Seat, Movie, Genre, Screening, Reservation, Ticket


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LandingPageView(View):
    def get(self, request):
        return render(request, 'landing_page.html')


class CinemaDetailsView(View):
    def get(self, request, cinema_id):
        cinema = Cinema.objects.get(pk=cinema_id)
        cnx = {'cinema': cinema}
        return render(request, "cinema_details.html", cnx)


class CinemaListView(View):
    def get(self, request):
        cinemas = Cinema.objects.all()
        cnx = {"cinemas": cinemas}
        return render(request, "cinema_list.html", cnx)


class CinemaAddView(View):
    def get(self, request):
        form = CinemaForm()
        return render(request, 'form/cinema_form.html', {'form': form})

    def post(self, request):
        form = CinemaForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            street = form.cleaned_data['street']
            postal_code = form.cleaned_data['postal_code']
            email = form.cleaned_data['email']
            telephone = form.cleaned_data['telephone']

            c = Cinema(city=city, street=street, postal_code=postal_code, email=email, telephone=telephone)
            c.save()

            response = "Added new cinema!"
        else:
            response = "Input correct data!"

        cnx = {
            "response": response
        }
        return render(request, 'form/form_response.html', cnx)


class HallAddView(View):
    def get(self, request, cinema_id):
        cinema = Cinema.objects.get(pk=cinema_id)
        form = HallForm()
        cnx = {
            'cinema': cinema,
            'form': form,
               }
        return render(request, 'form/hall_form.html', cnx)

    def post(self, request, cinema_id):
        form_again = HallForm()
        form = HallForm(request.POST)
        if form.is_valid():
            nr = form.cleaned_data['nr']
            seats_columns = form.cleaned_data['seats_columns']
            seats_rows = form.cleaned_data['seats_rows']
            cinema_id = form.cleaned_data['cinema_id']

            h = Hall(nr=nr, cinema_id=cinema_id, seats_columns=seats_columns, seats_rows=seats_rows)
            h.save()

            for seat in range(seats_columns * seats_rows):
                s = Seat(nr=seat, hall_id=h)
                s.save()

            response = f'{cinema_id.city}Hall {h.nr} Added!'

        else:
            response = "Hall not added"

        cnx = {
            'response': response,
            'form': form_again
            }
        return render(request, 'form/hall_form.html', cnx)
