from .views import ProjectViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register("projects", ProjectViewSet, basename="project")
