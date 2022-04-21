from django.urls import path
from .views import *

urlpatterns = [
   path('', show_posts),
   path('posts/', show_posts),
   path('create_post/', create_new_post),
   path('login/', login),
   path('test_form/', test_form)
   
]
