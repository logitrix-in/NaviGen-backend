import asyncio
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chatbot.vector_search.search import VectorSearcher as retriever
from chatbot.greetings.greetings import NaviGenAssistant as greetings


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "demo"
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        engine = retriever()
        result = await sync_to_async(engine.process_query)(message)
        message = result
        final_result = []
        for item in message:
            final_result.append(item)
            await self.send(text_data=json.dumps({"message": final_result}))
            await asyncio.sleep(0.01)


class GreetingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = "greeting"
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        engine = greetings()
        result = engine.get_response(message)
        for item in result:
            await self.send(text_data=json.dumps({"message": item}))
            await asyncio.sleep(0.1)
        engine2 = retriever()
        result2 = await sync_to_async(engine2.process_query)(message)
        collections = []
        for i in result2:
            collections.append(i.get("collection"))
            await self.send(text_data=json.dumps({"message": collections}))
            await asyncio.sleep(0.1)
        