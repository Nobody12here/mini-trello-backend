from rest_framework import serializers
from accounts.models import CustomUserModel
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ProjectMemberSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        queryset=CustomUserModel.objects.all(), many=True
    )

    class Meta:
        model = Project
        fields = ["members"]

    def create(self, instance):
        instance.members.add(instance.owner)

    def update(self, instance, validated_data):
        members = validated_data.get("members", [])
        if members:
            instance.members.add(*members)
        return instance
