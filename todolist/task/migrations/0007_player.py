# Generated by Django 4.1.3 on 2023-01-07 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0006_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('score', models.PositiveIntegerField()),
                ('position', models.CharField(max_length=50)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='task.file')),
            ],
        ),
    ]
