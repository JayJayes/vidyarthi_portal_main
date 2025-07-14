from djoser.serializers import UserSerializer as BaseUserSerializer
from frontend.models import CustomUser  # ✅ हे models चं location आहे
from rest_framework import serializers
from .models import CustomUser
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer

class CustomUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email','role')

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'password', 'role')