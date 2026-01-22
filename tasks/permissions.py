from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsProjectOwnerOrMember(BasePermission):
    def has_permission(self, request: Request, view):
        project_pk = view.kwargs.get("project_pk", None)
        if not project_pk:
            return False
        from projects.models import Project

        try:
            project: Project = Project.objects.get(pk=project_pk)
        except Project.DoesNotExist:
            return False
        user = request.user
        is_owner = project.owner == user
        is_member = project.members.filter(pk=user.pk).exists()

        if view.action in ["create", "destroy"]:
            return is_owner
        if view.action in ["list", "retrieve", "update", "partial_update"]:
            return is_owner or is_member

        return False
