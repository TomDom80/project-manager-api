from rest_framework import viewsets
from .models import Project, ProjectComment, ScopeOfWork, ContactPerson, ContactData
from .serializers import ProjectSerializer, ProjectCommentSerializer, ScopeOfWorkSerializer, ContactPersonSerializer, \
    ContactDataSerializer
from rest_framework.authentication import TokenAuthentication
from config.my_permissions import CustomDjangoModelPermission, IsOwnerOrReadOnly


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [CustomDjangoModelPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner_ID=self.request.user)


class ScopeOfWorkViewSet(viewsets.ModelViewSet):
    queryset = ScopeOfWork.objects.all()
    serializer_class = ScopeOfWorkSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner_ID=self.request.user)


class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [CustomDjangoModelPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner_ID=self.request.user)


class ContactDataViewSet(viewsets.ModelViewSet):
    queryset = ContactData.objects.all()
    serializer_class = ContactDataSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [CustomDjangoModelPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner_ID=self.request.user)


class ProjectCommentViewSet(viewsets.ModelViewSet):
    queryset = ProjectComment.objects.all()
    serializer_class = ProjectCommentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [CustomDjangoModelPermission, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner_ID=self.request.user)
