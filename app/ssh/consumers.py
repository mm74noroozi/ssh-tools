import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SecureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.host = self.scope['url_route']['kwargs']['host']
        self.room_group_name = 'chat_%s' % self.host

        # Join room group
        print(self.room_group_name,self.channel_name)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        # await self.send()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        host = text_data_json['host']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'toggle_host',
                'host': host
            }
        )

    # Receive message from room group
    async def toggle_host(self, event):
        host = event['host']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'host': host
        }))