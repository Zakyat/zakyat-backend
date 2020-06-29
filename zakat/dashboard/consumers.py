# Встроенные импорты.
import json

# Импорты сторонних библиотек.
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer

# Импорты Django.
from django.core.exceptions import ObjectDoesNotExist


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
       await self.channel_layer.group_add(
           'notification',
           self.channel_name
       )
       await self.accept()

    async def receive(self, text_data):
       await self.channel_layer.group_send(
            'notification',
            {
                'type': 'notify',
            }
        )

    async def notify(self, context):
        await self.send(text_data=json.dumps({
                'notification': context
            }))

    async def websocket_disconnect(self, message):
        await self.channel_layer.group_discard(
            'notification',
            self.channel_name
        )
