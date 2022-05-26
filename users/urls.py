from django.conf.urls import include
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')



urlpatterns = [
   path('api/users/register/', SignupAPIView.as_view()),
   path('api/', include(router.urls)),
]
