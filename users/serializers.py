from rest_framework import serializers
from .models import *

class AuthOKUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OKUser 
        fields = ('id', 'auth_token', 'first_name', 'last_name', 'date_created')
    
    
class OKUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OKUser 
        fields = ('id', 'first_name', 'last_name', 'date_created')