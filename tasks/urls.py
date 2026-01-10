from rest_framework_nested.routers import NestedDefaultRouter
from projects.urls import router as project_router
from .views import TaskViewset

router = NestedDefaultRouter(project_router, "projects", lookup="project")
router.register("tasks", TaskViewset, basename="project-task")
