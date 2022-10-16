from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostPageView(ListView):
    model = Post
    template_name = "post.html"
