import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ShowConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)
        self.accept()


    def disconnect(self, close_code):
        pass

    def chat_message(self, event):
        # Handles the "chat.message" event when it's sent to us.
        self.send(text_data=event["text"])
