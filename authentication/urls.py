from django.contrib import admin
from django.urls import path, include

from authentication.views import SignupView, LoginView
from django.contrib.auth import views

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login")
]
