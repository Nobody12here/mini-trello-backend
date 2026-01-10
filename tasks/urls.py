from rest_framework.routers import SimpleRouter
from rest_framework.urls import path
from .views import TaskViewSet

router = SimpleRouter()
router.register(r"tasks", TaskViewSet, basename="tasks")
