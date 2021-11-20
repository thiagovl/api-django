from rest_framework.exceptions import NotFound
from core.api.firebase_client import FirebaseClient
from core.api.serializers import ResumoSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

# Create your views here.

class ResumoViewSet(viewsets.ViewSet):
    client = FirebaseClient()

    def list(self, request):
        r = self.client.all()
        serializer = ResumoSerializer(r, many=True)
        return Response(serializer.data)
    
    @login_required(login_url='/login/')
    def retrieve(self, request, pk=None):
        resumo = self.client.get_by_id(pk)

        if resumo:
            serializer = ResumoSerializer(resumo)
            return Response(serializer.data)

    @login_required(login_url='/login/')
    def create(self, request, *args, **kwargs):
        serializer = ResumoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.create(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    @login_required(login_url='/login/')
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = ResumoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)

    @login_required(login_url='/login/')
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]