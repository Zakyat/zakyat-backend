import json
from channels.generic.websocket import AsyncWebsocketConsumer
from projects.models import Request
from payment.models import Transaction


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'notification',
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        unread_requests = Request.objects.filter(status='processing').count() + Request.objects.filter(
            status='negotiation').count()
        unread_transaction_count = Transaction.objects.count()
        await self.channel_layer.group_send(
            'notification',
            {
                'type': 'notify',
                'requests': unread_requests,
                'transaction': unread_transaction_count
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
