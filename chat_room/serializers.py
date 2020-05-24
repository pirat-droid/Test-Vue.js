from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Room, chat

class UserSerializers(serializers.ModelSerializer):
    """Сериализация поьзователей"""

    class Meta:
        model = User
        fields = ('id', 'username')

class RoomSerializers(serializers.ModelSerializer):
    """Сериализатор комнаты"""
    creater = UserSerializers()
    invited = UserSerializers(many=True)
    class Meta:
        model = Room
        fields = ('id', 'creater', 'invited', 'date')

class ChatSerializers(serializers.ModelSerializer):
    """Сериализация чата"""
    user = UserSerializers()
    class Meta:
        model = chat
        fields = ('user', 'text', 'date')

class ChatPostSerializers(serializers.ModelSerializer):
    """qwd"""
    class Meta:
        model = chat
        fields = ('room', 'text',)