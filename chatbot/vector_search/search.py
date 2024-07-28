from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from openai import OpenAI
from dotenv import load_dotenv
from django.apps import apps
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

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

    def getserializerclass(self, model_class):
        if not model_class:
            raise ObjectDoesNotExist(f"Model '{model_class}' does not exist.")

        class DynamicSerializer(serializers.ModelSerializer):
            class Meta:
                model = model_class
                fields = '__all__'

        return DynamicSerializer
    
    def search_collection_streamer(self, collection_name, query_embed):
        result = []

        all_models = apps.get_app_config('products').get_models()
        map_collection = {}
        for Model in all_models:
            map_collection[Model._meta.model_name.lower()] = Model

        for collection in collection_name:
            original_collection_model = map_collection[collection]            
            collection_serializer = self.getserializerclass(original_collection_model)
            db_results = self.client.search(collection_name=collection, query_vector=query_embed)
            answer = []
            for item in db_results:
                db = original_collection_model.objects.get(id=item.id)
                serializer = collection_serializer(db)
                answer.append(
                    {
                        "id": item.id,
                        "payload": serializer.data,
                    }
                )
                yield {
                    "collection": collection,
                    "results": answer
                }
                

    def search_collection(self, collection_name, query_embed):
        result = []

        all_models = apps.get_app_config('products').get_models()
        map_collection = {}
        for Model in all_models:
            map_collection[Model._meta.model_name.lower()] = Model

        for collection in collection_name:
            original_collection_model = map_collection[collection]            
            collection_serializer = self.getserializerclass(original_collection_model)
            db_results = self.client.search(collection_name=collection, query_vector=query_embed)
            answer = []
            for item in db_results:
                db = original_collection_model.objects.get(id=item.id)
                serializer = collection_serializer(db)
                answer.append(
                    {
                        "id": item.id,
                        "payload": serializer.data,
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

    def process_query_streamer(self, query):
        query_embed = self.encode_query(query)
        collections_list = self.get_collections_list()
        collection_name = self.choose_collection(query, collections_list)
        results = self.search_collection_streamer(collection_name, query_embed)
        for result in results:
            yield result
        