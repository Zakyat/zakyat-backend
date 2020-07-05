from channels.routing import ProtocolTypeRouter, URLRouter
from dashboard.routing import websockets

application = ProtocolTypeRouter({
    "websocket": websockets,
})
