from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, include

from authentication.views import SignupView, LoginView
from django.contrib.auth import views

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('password_change', PasswordChangeView.as_view(), name="password_change"),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name="password_change_done"),
    path('password_reset', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset/done/', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
