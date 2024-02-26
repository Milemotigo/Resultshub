from rest_framework import serializers
from .models import Colleges


class collegeSerializer(serializers.ModelSerializer):
    """"""
    class Meta:
        model = Colleges
        fields = '__all__'

    def create(self, validated_data):
        # Remove groups and user_permissions from validated_data
        groups_data = validated_data.pop('groups', [])
        user_permissions_data = validated_data.pop('user_permissions', [])

        # Create the Colleges instance
        college = Colleges.objects.create_user(**validated_data)

        # Add groups to the created Colleges instance
        for group_data in groups_data:
            college.groups.add(group_data)

        # Add user_permissions to the created Colleges instance
        for permission_data in user_permissions_data:
            college.user_permissions.add(permission_data)

        return college