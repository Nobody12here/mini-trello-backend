from django.urls import path
from .views import test_view

urlpatterns = [
    path("accounts/register", test_view),
    path("accounts/login", test_view),
]
