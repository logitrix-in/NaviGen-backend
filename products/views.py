from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from qdrant_client import QdrantClient

from sentence_transformers import SentenceTransformer


client = QdrantClient(
    url="https://9a693f2a-6a40-404d-8e21-4c732fed3fc5.eastus-0.azure.cloud.qdrant.io:6333/", 
    api_key="46NKKMjz4wjBE_rP6wFgpy6j9qe2Es4ekplgf27zEt7djEmnXnDESg",
)

model = SentenceTransformer(
    'all-MiniLM-L6-v2'
)

class Search(APIView):
    def get(self,req):
        query ="Show me some appliances"
        query_embed = model.encode(query)
        db = client.search(
            collection_name="all_appliances",
            query_vector=query_embed,
        )
        return Response(
            {
                "data":db
            }
        )