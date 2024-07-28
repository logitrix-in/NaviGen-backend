from django.urls import path

from .consumers import ChatConsumer, GreetingConsumer

websocket_urlpatterns = [
    path('query/', GreetingConsumer.as_asgi()),
    path('chat/', ChatConsumer.as_asgi()),
]
