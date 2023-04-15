from rest_framework.views import APIView
from rest_framework.response import Response

class HelloWorldApiView(APIView):

    def get(self,request,format=None):
        return Response("Hello World")