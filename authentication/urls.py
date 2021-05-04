from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from authentication.views import SignupView, LoginView
from django.contrib.auth import views

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout")
]
