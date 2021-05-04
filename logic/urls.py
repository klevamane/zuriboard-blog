from django.contrib import admin
from django.urls import path, include

from logic.views import IndexView, BlogView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('blog/<int:pk>', BlogView.as_view(), name="blog"),
]
