import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
from django.urls import path
from django.core.asgi import get_asgi_application

# Django settings configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS=['*']
INSTALLED_APPS=[
    'channels',
]
ASGI_APPLICATION='server.application'

django.setup()

# WebSocket consumer
class MyWebSocketConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data="WebSocket connection established.")

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        await self.send(text_data=f"Received: {text_data}")

# URL routing
websocket_urlpatterns = [
    path('', MyWebSocketConsumer.as_asgi()),
]

# ASGI application setup
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:application", host="0.0.0.0", port=8000, log_level="info")
