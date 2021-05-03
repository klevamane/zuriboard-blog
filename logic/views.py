from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from logic.models import Blog


class IndexView(View, ListView):
    model = Blog
    template = 'index.html'

