from django.db import models


class File(models.Model):
    """
    Class File
    """
    file = models.FileField(
        upload_to='files/',
        max_length=100,
        null=True, blank=True
    )


class Player(models.Model):
    """
    Class Player
    """
    file = models.ForeignKey(
        File,
        on_delete=models.CASCADE,
        related_name='player')
    name = models.CharField(max_length=200)
    score = models.PositiveIntegerField()
    position = models.CharField(max_length=50)
    results = models.TextField(max_length=500, default='champ')
