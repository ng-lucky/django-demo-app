from django.urls import path
from .views import *

urlpatterns = [
   path('posts/', show_posts)
]
