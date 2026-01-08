from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer, ProjectMemberSerializer
from .models import Project
from accounts.models import CustomUserModel

# Create your views here.


class ProjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    @action(detail=True, methods=["post"])
    def add_members(self, request: Request, pk=None):
        project = self.get_object()
        serializer = ProjectMemberSerializer(
            instance=project, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "message": "member added sucessfully",
            },
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"])
    def remove_members(self, request: Request, pk=None):
        project: Project = self.get_object()
        members = request.data.get("members", [])
        if members:
            members_ids = CustomUserModel.objects.filter(id__in=members).exclude(
                id=project.owner.id
            )
            project.members.remove(*members_ids)

        return Response(
            {"message": "Members removed sucessfully"}, status=status.HTTP_200_OK
        )
