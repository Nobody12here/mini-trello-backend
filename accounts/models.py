from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserModelManager

# Create your models here.


class CustomUserModel(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserModelManager()

    def __str__(self):
        return self.email
