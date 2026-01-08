from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from projects.urls import router as project_router

urlpatterns = [
    path("admin/", admin.site.urls),
    # JWT api's
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # Account App api
    path("api/", include("accounts.urls"), name="accounts"),
    path("api/", include(project_router.urls), name="project"),
    # Swagger docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        "api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="api-docs"
    ),
]
