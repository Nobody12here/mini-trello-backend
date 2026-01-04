from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view


schema_view = get_schema_view(
    openapi.Info(
        "mini-trello",
        "1.0.0",
        "A RESTful backend system where users can create projects, manage tasks, assign tasks to team members, and track task status.",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("accounts.urls"), name="accounts"),
    path("api/docs/", schema_view.with_ui("swagger", 0), name="api-docs"),
]
