import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Gatherings


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'notification',
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        unread_gatherings_count = Gatherings.objects.count()
        await self.channel_layer.group_send(
            'notification',
            {
                'type': 'notify',
                'gathering': unread_gatherings_count
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
