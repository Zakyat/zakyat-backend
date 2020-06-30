from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import NotificationConsumer

websockets = URLRouter([
    path(
        "ws/notification/", NotificationConsumer,
        name="live-score",
    ),
])
