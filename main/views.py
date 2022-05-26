from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from demo_app.pagination import ResultsPagination
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *


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


class PostAPIView(APIView):
    def get(self, request):
        
        posts = [post.title for post in Post.objects.all()]
        # for post in Post.objects.all():
        #     posts.append(post.title)
            
        return Response(posts)
    
    def post(self, request):
        title = request.data.get("title")
        body = request.data.get("body")
        photo_url = request.data.get("photo_url")
        post = Post.objects.create(
            title = title,
            body=body,
            photo_url=photo_url
        )
        post.save()
        return Response({"message": "Post succesfully created", "status": True}, status=201)

class PostViewSet(viewsets.ModelViewSet):

    @action(methods=["POST"], detail=False)
    def create_post(self, request):
        title = request.data.get("title")
        body = request.data.get("body")
        photo_url = request.data.get("photo_url")
        post = Post.objects.create(
            title = title,
            body=body,
            photo_url=photo_url
        )
        post.save()
        return Response({"message": "Post succesfully created", "status": True}, status=201)
    @action(methods=["POST"], detail=False,permission_classes=[AllowAny])
    def filter_post(self, request):
        search_text = request.data.get("search_text")
        paginator = ResultsPagination()
        
        
        queryset = Post.objects.all()
        if search_text and search_text != '':
            queryset = queryset.filter(title__contains=search_text)
        
        paginated_result = paginator.paginate_queryset(queryset, request)
        serializer = PostSerializer(paginated_result, many=True)
        
        return paginator.get_paginated_response(serializer.data)