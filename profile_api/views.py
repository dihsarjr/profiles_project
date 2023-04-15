from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api.serializers import HelloSerializer


class HelloWorldApiView(APIView):

    serializer_class = HelloSerializer

    def get(self, request, format=None):
        return Response("Hello World")

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response({'error': serializer.errors, 'error_message': serializer.error_messages},
                            status=status.HTTP_400_BAD_REQUEST)
