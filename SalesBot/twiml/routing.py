# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path("audiostream", consumers.ChatConsumer.as_asgi()),
]