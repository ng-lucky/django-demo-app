from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('create_post/<str:post>/', create_post)
]
