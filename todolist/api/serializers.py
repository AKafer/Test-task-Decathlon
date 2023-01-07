from rest_framework import serializers

from task.models import File, Player


class FileSerializer(serializers.ModelSerializer):
    """Класс сериализатора файлов."""

    class Meta:
        fields = '__all__'
        model = File


class PlayerSerializer(serializers.ModelSerializer):
    """Класс сериализатора файлов."""

    class Meta:
        fields = '__all__'
        model = Player
