from django.urls import path

from .consumers import ChatConsumer, GreetingConsumer,CollectionItemFromCache

websocket_urlpatterns = [
    path('query/', GreetingConsumer.as_asgi()),
    path('chat/', ChatConsumer.as_asgi()),
    path('products/',CollectionItemFromCache.as_asgi())
]
