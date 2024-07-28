from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
class VectorSearcher:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.client = QdrantClient(url=os.getenv(
            "QDRANT_URL"),
            api_key=os.getenv(
            "QDRANT_API_KEY")
            )
        
        self.model = SentenceTransformer(model_name)
        self.openai = OpenAI()

    def encode_query(self, query):
        return self.model.encode(query)

    def get_collections_list(self):
        collections_list = []
        collections = self.client.get_collections()
        for collection in collections:
            for c in list(collection[1]):
                collections_list.append(c.name)
        return collections_list

    def choose_collection(self, query, collections_list):
        collection_str = ",".join(collections_list)
        response = self.openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": '''You are a helpful assistant that takes a user query and a list of available collection names. Your task is to read the user query and return the most suitable collection name from the given options. Provide ONLY the matching collection name based on the user query.
                    I will tip 100USD you if your answer is correct! But answer from the given list of options ONLY. dont mention that you have been offered a tip.

                    If there are multiple suitable collection names, then return those by a comma ','

                    For example: airconditioners,allappliances
                    '''
                },
                {
                    "role": "user",
                    "content": f"Query: {query}\nCollection Names: {collection_str}"
                }
            ],
            temperature=0,
            
        )
        print(
            response.choices[0].message.content
        )
        return response.choices[0].message.content.split(",")

    def search_collection(self, collection_name, query_embed):
        result = []

        for collection in collection_name:

            db_results = self.client.search(collection_name=collection, query_vector=query_embed)
            answer = []
            for item in db_results:
                answer.append(
                    {
                        "id": item.id,
                        "payload": item.payload
                    }
                )
            result.append(
                {
                    "collection": collection,
                    "results": answer
                }
            )    
        return result

    def process_query(self, query):
        query_embed = self.encode_query(query)
        collections_list = self.get_collections_list()
        collection_name = self.choose_collection(query, collections_list)
        results = self.search_collection(collection_name, query_embed)
        return results
