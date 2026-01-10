from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .serializers import ProjectSerializer, ProjectMemberSerializer
from .models import Project
from accounts.models import CustomUserModel


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        owner = self.request.user
        return Project.objects.filter(owner=owner)

    def perform_create(self, serializer: ProjectSerializer):
        project: Project = serializer.save(owner=self.request.user)
        project.members.add(project.owner)
        return project

    @action(detail=True, methods=["post"])
    def add_members(self, request: Request, pk=None):
        project: Project = self.get_object()
        serializer = ProjectMemberSerializer(
            instance=project, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "member added successfully",
            },
            status=status.HTTP_204_NO_CONTENT,
        )

    @action(detail=True, methods=["post"])
    def remove_members(self, request: Request, pk=None):
        project: Project = self.get_object()
        members = request.data.get("members", [])
        if members:
            member_ids = CustomUserModel.objects.filter(id__in=members).exclude(
                id=project.owner.id
            )
            project.members.remove(*member_ids)
        else:
            return Response(
                {"error": "No member ids provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            {"message": "Members removed successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
