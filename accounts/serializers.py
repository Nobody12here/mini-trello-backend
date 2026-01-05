from .models import CustomUserModel
from rest_framework import serializers


class AccountRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ["email"]
