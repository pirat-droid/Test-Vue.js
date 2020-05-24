import chat as chat
# Для сождания запроса или
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib.auth.models import User

from .models import Room, chat
from .serializers import RoomSerializers, ChatSerializers, ChatPostSerializers, UserSerializers


class RoomView(APIView):
    """Комнаты чата"""
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        rooms = Room.objects.filter(Q(creater=request.user) | Q(invited=request.user))
        serializer = RoomSerializers(rooms, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        Room.objects.create(creater=request.user)
        return Response(status=201)

class DialogView(APIView):
    """Диалог чата"""
    # для    авторизованных    пользователей
    permission_classes = [permissions.IsAuthenticated, ]

    # Для всех пользователей
    # permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        room = request.GET.get('room')
        chatik = chat.objects.filter(room=room)
        serializer = ChatSerializers(chatik, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # room = request.data.get('room')
        dialog = ChatPostSerializers(data=request.data)
        if dialog.is_valid():
            dialog.save(user=request.user)
            return Response(status=201)
        else:
            return Response(status=400)


class AddUsersRoomView(APIView):
    """Добавление пользователей в комнату"""

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        room = request.data.get('room')
        user = request.data.get('user')
        try:
            room = Room.objects.get(id=room)
            room.invited.add(user)
            room.save()
            return Response(status=201)
        except:
            return Response(status=400)
