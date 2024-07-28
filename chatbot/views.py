from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import os

# Create your views here.
class GreetingsView(APIView):
    def get(self, request):
        query = request.GET.get('query', None)
        if query:
            from openai import OpenAI
            client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
            # Example OpenAI Python library request
            MODEL = "gpt-3.5-turbo"
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant who actually greets the user and helps them with their queries. Your name is NaviGen. Provide sugessions for any products based on user queries. You can only suggest items from your own shop. Do not mention the names of other shopping stores or websites. Do not give the names of the products which you are suggesting, only your greeting message is important. Giving you an example how you should reply. ``` user: I am here to find a gift for my 19 year old kid. assistant: Welcome to NaviGen, your ultimate AI-powered shopping asisstant. We're here to help you find the perfect gift for your 19 year old kid. Based on popular trends and what young adults love, here are some great gift ideas: ``` Now, it's your turn to reply to the user's query.``` If you are asked any irrelevant question, you can reply with 'I am sorry, I am not able to help with that.' along with a short intro about yourself.```"},
                    
                    {"role": "user", "content" : query}
                ],
                temperature=0,
            )


            return Response({"message": response.choices[0].message.content})


        return Response({"message": "Hello, World!"})