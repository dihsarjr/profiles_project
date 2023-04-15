from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_api.serializers import HelloSerializer, UserProfileSerializer
from profile_api import models
from rest_framework.authentication import TokenAuthentication
from profile_api import permissions
from rest_framework import filters


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


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
