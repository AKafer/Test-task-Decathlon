from django.contrib import admin

from .models import File, Player

admin.site.register(Player)
admin.site.register(File)
