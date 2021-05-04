from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView

from logic.forms import CommentForm
from logic.models import Blog


class IndexView(ListView):
    model = Blog
    template_name = 'logic/blog_list.html'

    context_object_name = 'blog_list'


class BlogView(View):

    template_name = 'logic/blog.html'
    blogg = None

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)

        self.blogg = blog
        return render(
            request=request,
            template_name=self.template_name,
            context={
                "blog": blog,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.blog = blog
            instance.user = request.user
            instance.save()
            return redirect("blog", pk)
