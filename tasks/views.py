from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwnerOrMember
from .serializers import TaskSerializer
from .models import Task


class TaskViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, IsProjectOwnerOrMember]
    serializer_class = TaskSerializer

    def get_queryset(self):
        print(self.request.user.id)
        return Task.objects.filter(project=self.kwargs["project_pk"])

    def perform_create(self, serializer):
        from projects.models import Project

        project = Project.objects.get(pk=self.kwargs["project_pk"])
        serializer.save(project=project)
