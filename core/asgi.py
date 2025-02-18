# filepath: /home/daviga/projects/mqtt-app/mqtt_app/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from features.subscribe.services.consumer import MqttConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mqtt_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/mqtt/", MqttConsumer.as_asgi()),
        ])
    ),
})