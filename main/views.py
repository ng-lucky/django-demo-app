from django.http import HttpResponse
from django.shortcuts import render

from .models import *

# Create your views here.
def index(request):
    tests = TestModel.objects.all()
    return render(request, 'index.html', {'tests': tests})

def create_post(request, post):
    test = TestModel.objects.create(
        name=post
    )
    test.save()
    return HttpResponse("<h1>Post successfully created</h1>")


def show_posts(request):
    posts = Post.objects.all()
    return render(request,"posts_list.html", {"posts_list": posts})


def create_new_post(request):
    post = Post.objects.create(
        title = "My post tiltle",
        body = "My new post body",
        photo_url = "wwww.eagaloe1.com/photo.png"
    )
    post.save()
    return HttpResponse("<h2>Post created </h2>")

def login(request):
    return render(request, "login.html")
