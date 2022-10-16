from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy


class HomePageView(TemplateView):
    template_name = "index.html"


class PostPageView(TemplateView):  # new
    template_name = "post.html"


class PostsPageViewList(ListView):  # new
    model = Post
    template_name = "posts.html"


class CreatePageView(CreateView):  # new
    model = Post
    template_name = "create.html"
    fields = ["title", "author", "body"]
    success_url = reverse_lazy("create")
