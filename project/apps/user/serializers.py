from rest_framework import serializers

from project.apps.core.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')

    class Meta:
        model = User
        fields = ('code', 'full_name')