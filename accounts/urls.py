from django.urls import path
from .views import test_view, register_user

urlpatterns = [
    path("accounts/register", register_user, name="register-user"),
    path("accounts/login", test_view),
]
