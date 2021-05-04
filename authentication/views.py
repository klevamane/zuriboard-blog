from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import SignupForm
from authentication.models import User


class SignupView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "authentication/register.html"
    form_class = SignupForm
    success_url = reverse_lazy("index")
    success_message = 'Registration was successful'


