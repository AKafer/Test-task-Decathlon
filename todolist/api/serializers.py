from rest_framework import serializers

from task.models import File, Player


class FileSerializer(serializers.ModelSerializer):
    """Class serializer for files."""

    class Meta:
        fields = '__all__'
        model = File


class PlayerSerializer(serializers.ModelSerializer):
    """Class serializer for players."""

    class Meta:
        fields = '__all__'
        model = Player
