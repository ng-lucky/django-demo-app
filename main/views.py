from django.http import HttpResponse
from django.shortcuts import render

from .forms import *

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
    form = PostFormNew()
    message = ''
    if request.method == 'POST':
        form = PostFormNew(request.POST)
        if form.is_valid:
            print(form)
            title = form.cleaned_data["title"]
            body = form.cleaned_data["body"]
            photo_url = form.cleaned_data["photo_url"]
            
            post = Post.objects.create(
                title = title,
                body = body,
                photo_url = photo_url
            )
            post.save()
            message = 'Post created'
        
    return render(request, "create_post.html", {"form": form, "message": message})

def login(request):
    return render(request, "login.html")

def test_form(request):
    form = TestForm()
    reply = ''
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            message = form.cleaned_data["message"]
            testm = TestModel.objects.create(
                name=name,
                message = message
            )
            testm.save()
            reply = 'Message sent successfully'
    return render(request, "test.html", {"form": form, "reply": reply})
