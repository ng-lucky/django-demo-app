from django.http import HttpResponse
from django.shortcuts import render

from main.models import TestModel

# Create your views here.
def index(request):
    tests = TestModel.objects.all()
    return render(request, 'index.html', {'tests': tests})

def create_post(request, post):
    test = TestModel.objects.create(
        name=post
    )
    test.save()
    return HttpResponse("Post successfully created")