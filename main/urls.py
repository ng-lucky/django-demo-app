from django.urls import path
from .views import *

urlpatterns = [
   path('posts/', show_posts),
   path('create_post/', create_new_post),
   path('login/', login)
]
