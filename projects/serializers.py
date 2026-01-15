from rest_framework import serializers
from accounts.models import CustomUserModel
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ['owner']


class ProjectMemberSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        queryset=CustomUserModel.objects.all(), many=True
    )

    class Meta:
        model = Project
        fields = ["members"]

    def update(self, instance, validated_data):
        members = validated_data.get("members", [])
        if members:
            instance.members.add(*members)
        return instance
