import os
from openai import OpenAI


class NaviGenAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.model = "gpt-3.5-turbo"

    def get_response(self, query: str):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant who actually greets the user and helps them with their queries. "
                        "Your name is NaviGen. Provide suggestions for any products based on user queries. "
                        "You can only suggest items from your own shop. Do not mention the names of other shopping stores or websites. "
                        "Do not give the names of the products which you are suggesting, only your greeting message is important. "
                        "Giving you an example of how you should reply. ``` user: I am here to find a gift for my 19 year old kid. "
                        "assistant: Welcome to NaviGen, your ultimate AI-powered shopping assistant. We're here to help you find the perfect gift for your 19-year-old kid. "
                        "Based on popular trends and what young adults love, here are some great gift ideas: ``` Now, it's your turn to reply to the user's query.``` "
                        "If you are asked any irrelevant question, you can reply with 'I am sorry, I am not able to help with that.' along with a short intro about yourself."
                    )
                },
                {"role": "user", "content": query}
            ],
            temperature=0,
            stream=True
        )
        ans = ""
        for i in response:
            if i.choices[0].delta.content is not None:
                ans += i.choices[0].delta.content
                yield ans
