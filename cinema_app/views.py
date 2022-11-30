import django
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View, generic, decorators
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LandingPage(View):
    def get(self, request):
        return render(request, 'landing_page.html')


class AddCinema(View):
    def get(self, request):
        return render(request, 'cinema_form.html')

    @csrf_exempt
    def post(self, request):
        cnx = {}
        return render(request, 'add_cinema', cnx)
