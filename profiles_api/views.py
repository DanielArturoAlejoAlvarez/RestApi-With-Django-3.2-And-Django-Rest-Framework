from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    def get(self, request, format=None):

        an_apiview = [
            'We use HTTP methods like get,post,put,patch,delete,etc',
            'It is similar a to traditional view in django',
            'It gives us greater control over the logic of the application',
            'It is manually mapped to Urls'
        ]

        return Response({
            'msg': 'Hello World!', 
            'an_apiview': an_apiview
        })

