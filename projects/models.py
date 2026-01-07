from django.db import models
from accounts.models import CustomUserModel


class Project(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True, default="")
    owner = models.ForeignKey(
        CustomUserModel, related_name="project_owner", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(CustomUserModel, related_name="project_members")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name} - {self.owner}"
