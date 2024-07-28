from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from chatbot.vector_search.search import VectorSearcher as retriever
    
class GetSuggestion(APIView):
    def get(self,request):
        query=request.GET.get('query',None)
        if query:
            searcher=retriever()
            result=searcher.process_query(query)
            return Response(
                {
                    "data":result
                }
            )


        else:
            return Response(
                {
                    "data":"Please provide query"
                }
            )