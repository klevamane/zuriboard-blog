from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from logic.models import Blog


class IndexView(ListView):
    model = Blog
    template_name = 'logic/blog_list.html'

    context_object_name = 'blog_list'

