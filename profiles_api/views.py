from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from profiles_api import serializers

class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer


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

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hello {name}'

            return Response({
                'msg': msg
            })

        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        return Response({'method': 'PUT'})


