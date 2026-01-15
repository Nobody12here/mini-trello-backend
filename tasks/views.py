from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task





class TaskViewset(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(project=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)