from django.urls import path
from .views import *

urlpatterns = [
    path('room/', RoomView.as_view()),
    path('dialog/', DialogView.as_view()),
    path('users/', AddUsersRoomView.as_view()),
]