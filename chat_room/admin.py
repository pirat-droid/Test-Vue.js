from django.contrib import admin

from .models import Room, chat

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Комната чата"""
    list_display = ('creater', 'invited_user', 'date')

    def invited_user(self, obj):
        return "\n".join([user.username for user in obj.invited.all()])

@admin.register(chat)
class ChatAdmin(admin.ModelAdmin):
    """Диалоги"""
    list_display = ('room', 'user', 'text', 'date',)

