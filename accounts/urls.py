from django.urls import path
from .views import login, register_user

urlpatterns = [
    path("accounts/register", register_user, name="register-user"),
    path("accounts/login", login, name="login"),
]
