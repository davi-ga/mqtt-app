# filepath: /home/daviga/projects/mqtt-app/mqtt_app/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime

class MqttConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("mqtt_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("mqtt_group", self.channel_name)

    async def receive(self, text_data):
        pass

    async def mqtt_message(self, event):
        message = event['message']
        topic = event['topic']
        timestamp = datetime.now().isoformat()
        await self.send(text_data=json.dumps({
            "topic": topic,
            'message': message,
            "timestamp": timestamp
        }))