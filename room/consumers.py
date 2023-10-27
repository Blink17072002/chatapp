import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Room, Message
from chat.models import User


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender = data['sender']
        room = data['room']
        avatar = data['avatar']
        
        await self.save_message(sender, message, room, avatar)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': sender,
                'room': self.room_name,
                'avatar': avatar,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        room = event['room']
        avatar = event['avatar']
        

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'room': room,
            'avatar': avatar,
        }))

    @sync_to_async
    def save_message(self, sender, message, room, avatar):
        user = User.objects.get(username=sender)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, room=room, content=message)