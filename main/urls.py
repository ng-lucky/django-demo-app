from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
   path('', show_posts),
   path('posts/', show_posts),
   path('create_post/', create_new_post),
   path('login/', login),
   path('test_form/', test_form),
   path('api/posts/', PostAPIView.as_view()),
   path('api/', include(router.urls)),
]
