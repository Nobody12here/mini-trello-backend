from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from projects.permissions import IsOwner
from .models import Task


class TaskViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ""
    queryset = Task.objects.all()
