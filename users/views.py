import re
from django.shortcuts import render
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from rest_framework.status import (HTTP_101_SWITCHING_PROTOCOLS, HTTP_201_CREATED,
                                   HTTP_100_CONTINUE,
                                   HTTP_200_OK,
                                   HTTP_203_NON_AUTHORITATIVE_INFORMATION,
                                   HTTP_304_NOT_MODIFIED,
                                   HTTP_204_NO_CONTENT,
                                   HTTP_400_BAD_REQUEST, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,
                                   HTTP_500_INTERNAL_SERVER_ERROR)
# Create your views here.



class UserViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email:
            return Response({"message": "Crazy guy!!!, how do you login without email"}, status=HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"message": "Get out!! send me a password"}, status=HTTP_400_BAD_REQUEST)
        
        try:
            user = OKUser.objects.get(email = email, is_active=True)
            if user.is_blocked == False:
                # login user here
                auth_user = authenticate(email=email, password=password)
                login(request, auth_user)
                serializer = AuthOKUserSerializer(instance=auth_user, many=False)
                return Response({"results": serializer.data}, status=HTTP_200_OK)
            else:
                return Response({"message": "Kommot for dere!!"}, status=HTTP_400_BAD_REQUEST)
                
        except OKUser.DoesNotExist:
            return Response({"message": "You be ghost? I don't know you"}, status=HTTP_400_BAD_REQUEST)
        
    

class SignupAPIView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or email == '':
            return Response({"detail": "Please provide valid email"}, status=400)
        
        try:
            user = OKUser.objects.get(email=email)
            if user:
                return Response({"detail": "Email already exists"}, status=400)
        except OKUser.DoesNotExist:
            myuser = OKUser.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email
            )
           
            myuser.set_password(password)
            myuser.save()
            # send email verification emails, or welcomoe emails
            
            return Response({'detail': 'Your account has been successfully created. An email has been sent to {}, follow the link in there to verify your email'.format(email), "status": True})