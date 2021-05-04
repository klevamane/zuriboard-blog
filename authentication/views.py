from django.contrib import messages
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

    def form_valid(self, form):
        # runs if the form is valid

        return super().form_valid(form)

    def form_invalid(self, form):
        # import pdb; pdb.set_trace()
        for k, err in form.errors.items():
            messages.error(self.request, err[0])
        return super().form_invalid(form)


