from rest_framework.views import APIView
from rest_framework.response import Response
from microservice_lambda.models import ProductModel
from microservice_lambda.serializers import ProductSerializer
import json

from django.http import HttpResponse
 

class ProductViewAPI(APIView):

    def get(self, request, format=None):
        
        snippets = ProductModel.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        serializer_data = serializer.data
        return Response(serializer_data)

    def post(self, request, format=None):

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
            
        return Response(serializer.errors, status=400)


def APIListViewAPI( request, format=None):
        
        apis = {
            'Get all Products' : {
                'Method' : 'GET',
                'Path' :  '/dev/products/'
            },
            'Create Product' : {
                'Method' : 'POST',
                'Path' :  '/dev/products/'
            },
        }
        response = json.dumps(apis, indent=2) 
        return HttpResponse(response)