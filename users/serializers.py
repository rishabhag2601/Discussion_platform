

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile_no', 'followers']
        ref_name = 'CustomUserSerializer'
# users/serializers.py

from djoser.serializers import UserSerializer as DjoserUserSerializer

class CustomDjoserUserSerializer(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        ref_name = 'DjoserUserSerializer'
