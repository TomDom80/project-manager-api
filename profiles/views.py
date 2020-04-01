from django.contrib.auth.models import User
from .serializers import UserSerializer, CurrentUserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)


class CurrentUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(id=-1)
    serializer_class = CurrentUserSerializer

    def list(self, request):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
