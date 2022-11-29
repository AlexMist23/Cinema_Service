from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import View, generic
from django.urls import reverse_lazy


class LandingPage(View):
    def get(self, request):
        return render(request, 'landing_page.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
