from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView

from polls.models import Post

def index(request):
    return HttpResponse("Hello World")

class BlogListView(ListView):
    model = Post
    template_name="polls/home.html"
# Create your views here.
