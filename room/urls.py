from django.urls import path
from . import views

app_name = 'room'

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('create-room/', views.create_room, name='create_room'),
    path('<slug:slug>/', views.room_messages, name='room_messages'),
]
