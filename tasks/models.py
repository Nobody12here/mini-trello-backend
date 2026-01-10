from django.db import models
from projects.models import Project


class Task(models.Model):
    class TaskStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETE = "complete", "Complete"
        IN_PROGRESS = "working", "In Progress"

    class TaskPriority(models.IntegerChoices):
        NORMAL = 1, "Normal"
        URGENT = 2, "Urgent"
        CRITICAL = 3, "Critical"

    name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=True, default="")
    project = models.ForeignKey(
        Project, null=True, on_delete=models.SET_NULL, related_name="project"
    )
    status = models.CharField(
        choices=TaskStatus.choices,
        max_length=20,
        default=TaskStatus.PENDING,
        db_index=True,
    )
    priority = models.PositiveSmallIntegerField(
        choices=TaskPriority.choices, default=TaskPriority.NORMAL
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
