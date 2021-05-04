from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from authentication.forms import SignupForm, LoginForm
from authentication.models import User
from django.contrib.auth import views


class SignupView(SuccessMessageMixin, CreateView):
    model = User
    template_name = "authentication/register.html"
    form_class = SignupForm
    success_url = reverse_lazy("index")
    success_message = 'Registration was successful'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("index")
        return super(SignupView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        # runs if the form is valid

        return super().form_valid(form)

    def form_invalid(self, form):
        # import pdb; pdb.set_trace()
        for k, err in form.errors.items():
            messages.error(self.request, err[0])
        return super().form_invalid(form)


class LoginView(SuccessMessageMixin, views.LoginView):
    template_name = "authentication/login.html"
    success_url = reverse_lazy("index")
    form_class = LoginForm

    def form_invalid(self, form):
        for k, err in form.errors.items():
            messages.error(self.request, err[0])

        return super().form_invalid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect("index")
        return super(LoginView, self).get(request, *args, **kwargs)

